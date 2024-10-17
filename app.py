from flask import Flask, render_template, request, redirect, url_for, flash, session

# Import boundary objects
from boundary.user_login_boundary import UserLoginBoundary
from boundary.user_signup_boundary import UserSignupBoundary
from boundary.weather_boundary import WeatherBoundary
from boundary.feedback_boundary import FeedbackBoundary
from boundary.dashboard_settings_boundary import DashboardSettingsBoundary
from boundary.alert_boundary import AlertBoundary
from boundary.data_export_boundary import DataExportBoundary
from boundary.educational_content_boundary import EducationalContentBoundary
from boundary.extended_forecast_boundary import ExtendedForecastBoundary
from boundary.today_forecast_boundary import TodayForecastBoundary
from boundary.historical_data_boundary import HistoricalDataBoundary
from boundary.health_advisory_boundary import HealthAdvisoryBoundary
from boundary.reset_password_boundary import ResetPasswordBoundary
from boundary.faq_boundary import FAQBoundary

# Import control objects
from controls.feedback_control import FeedbackControl
from controls.dashboard_settings_control import DashboardSettingsControl
from controls.alert_control import AlertControl
from controls.data_Export_control import DataExportControl
from controls.health_advisory_control import HealthAdvisoryControl
from controls.reset_password_control import ResetPasswordControl
from HU.Project.Website.controls.user_login_control import UserLoginControl
from HU.Project.Website.controls.user_signup_control import UserSignupControl

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Use a secure key in production


# Helper function for login checks
def login_required():
    if not session.get('username'):
        flash('You need to log in to access this page.', 'danger')
        return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():
    # Use Boundary to handle user input
    boundary = UserLoginBoundary()

    # Check if user is logged in
    logged_in = 'username' in session

    if request.method == 'POST':
        if 'login' in request.form:
            # Boundary object retrieves username and password from request
            username, password = boundary.login(request)

            # Control object handles authentication logic
            control = UserLoginControl()
            if control.authenticate(username, password):
                session['username'] = username
                session['user_id'] = control.get_user_id(username)
                flash('Login successful!', 'success')
                return redirect(url_for('home'))  # Reload to prevent form resubmission
            else:
                flash('Invalid credentials', 'danger')

        elif 'signup' in request.form:
            # Use boundary object to handle signup data collection
            boundary = UserSignupBoundary()
            username, email, password, confirm_password, address, location = boundary.signup(request)

            # Control handles business logic for signup
            control = UserSignupControl()
            if password != confirm_password:
                flash('Passwords do not match!', 'danger')
            else:
                success = control.signup(username, email, password, address, location)
                if success:
                    flash('Signup successful! Please log in.', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Signup failed. Please try again.', 'danger')

    # Render the homepage, passing login state
    return render_template('home.html', logged_in=logged_in, username=session.get('username'))


# Route for Viewing Latest Weather
@app.route('/weather', methods=['GET', 'POST'])
def view_weather():
    boundary = WeatherBoundary()

    if request.method == 'POST':
        weather_data, location = boundary.get_latest_weather(request)
        return render_template('weather.html', weather=weather_data, location=location)

    return render_template('weather.html')


# Route for Today's Forecast
@app.route('/today_forecast', methods=['GET'])
def view_today_forecast():
    boundary = TodayForecastBoundary()

    forecast_data = boundary.get_today_forecast(request)
    location = request.args.get('location', 'New York')
    return render_template('today_forecast.html', forecast=forecast_data, location=location)


# Route for Extended Forecast
@app.route('/extended_forecast', methods=['GET'])
def view_extended_forecast():
    boundary = ExtendedForecastBoundary()

    extended_forecast_data = boundary.get_extended_forecast(request)

    location = request.args.get('location', 'New York')
    days = request.args.get('days', 7, type=int)
    return render_template('extended_forecast.html', forecast=extended_forecast_data, location=location, days=days)


# Route for Viewing Historical Weather Data
@app.route('/historical_data', methods=['GET'])
def view_historical_data():
    boundary = HistoricalDataBoundary()

    historical_data = boundary.get_historical_data(request)
    location = request.args.get('location', 'New York')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    return render_template('historical_data.html', historical_data=historical_data, location=location, start_date=start_date, end_date=end_date)


# Route for FAQ
@app.route('/faq')
def faq():
    boundary = FAQBoundary()

    faqs = boundary.get_faqs()
    return render_template('faq.html', faqs=faqs)


# Route for Educational Content
@app.route('/educational_content')
def view_educational_content():
    boundary = EducationalContentBoundary()

    content = boundary.get_content(request)
    topic = boundary.get_content('topic')
    return render_template('educational_content.html', content=content)


# Route for Alerts and Health Advisories
@app.route('/alerts', methods=['GET', 'POST'])
def manage_alerts():
    if not session.get('username'):
        return login_required()

    boundary = AlertBoundary()
    control = AlertControl()

    if request.method == 'POST':
        alert_type, condition = boundary.create_alert(request)
        control.create_alert(session.get('user_id'), alert_type, condition)
        flash('Alert created successfully!', 'success')

    user_location = session.get('user_location', 'New York')
    alerts = control.get_user_alerts(session.get('user_id'))
    advisories = control.check_health_advisory(session.get('user_id'))

    return render_template('alerts.html', alerts=alerts, advisories=advisories)


# Route for Dashboard Customization
@app.route('/customize_dashboard', methods=['GET', 'POST'])
def customize_dashboard():
    if not session.get('username'):
        return login_required()

    boundary = DashboardSettingsBoundary()
    control = DashboardSettingsControl()

    if request.method == 'POST':
        # Use boundary to extract the settings from the form
        settings = boundary.save_dashboard_settings(request)

        # Pass the settings to the control object for saving
        control.save_settings(session['user_id'], settings)
        flash('Dashboard settings saved!', 'success')

    # Load the current dashboard settings
    current_settings = control.load_dashboard_settings(session['user_id'])
    return render_template('dashboard.html', settings=current_settings)


# Route for Submitting Feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    # Check if the user is logged in
    if not session.get('username'):
        return login_required()

    boundary = FeedbackBoundary()

    if request.method == 'POST':
        # Use boundary to get feedback details
        feedback_type, message = boundary.submit_feedback(request)

        # Use control to process feedback
        control = FeedbackControl()
        control.submit_feedback(session['user_id'], session['username'], feedback_type, message)
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('feedback.html')


# Route for Exporting Data
@app.route('/export', methods=['GET', 'POST'])
def export_data():
    if not session.get('username'):
        return login_required()

    boundary = DataExportBoundary()
    control = DataExportControl()

    if request.method == 'POST':
        export_format, location, start_date, end_date = boundary.export_data(request)
        file_path = control.export_data(session['user_id'], export_format, location, start_date, end_date)
        flash(f'Data exported successfully! Download at: {file_path}', 'success')
    return render_template('export.html')


# Route for Reset Password
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    boundary = ResetPasswordBoundary()

    if request.method == 'POST':
        username, new_password = boundary.reset_password(request)
        print(username, new_password)
        control = ResetPasswordControl()
        if control.reset_password(username, new_password):
            flash('Password reset successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Error resetting password', 'danger')

    return render_template('reset_password.html')


# Route for Logout
@app.route('/logout')
def logout():
    session.clear()  # Clears all session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
