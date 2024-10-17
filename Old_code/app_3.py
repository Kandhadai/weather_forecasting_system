from flask import Flask, render_template, request, redirect, url_for, flash, session

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

# Import the control objects
from controls.user_login_control import UserLoginControl
from controls.user_signup_control import UserSignupControl
from controls.weather_control import WeatherControl
from controls.feedback_control import FeedbackControl
from controls.dashboard_settings_control import DashboardSettingsControl
from controls.alert_control import AlertControl
from controls.data_Export_control import DataExportControl
from controls.educational_content_control import EducationalContentControl
from controls.view_extended_forecast_control import ExtendedForecastControl
from controls.view_today_forecast_control import TodayForecastControl
from controls.view_historical_data_control import HistoricalDataControl
from controls.health_advisory_control import HealthAdvisoryControl
from controls.reset_password_control import ResetPasswordControl
from controls.faq_control import FAQControl

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Use a secure key in production

# Helper function for login checks
def login_required():
    if not session.get('username'):
        flash('You need to log in to access this page.', 'danger')
        return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST'])
def home():
    control = UserLoginBoundary()

    # Check if user is logged in
    logged_in = 'username' in session

    if request.method == 'POST':
        if 'login' in request.form:
            # Handle login
            username = request.form['username']
            password = request.form['password']
            control_obj = UserLoginControl()
            if control_obj.authenticate(username, password):
                session['username'] = username
                session['user_id'] = control_obj.get_user_id(username)
                flash('Login successful!', 'success')
                return redirect(url_for('home'))  # Reload to prevent form resubmission
            else:
                flash('Invalid credentials', 'danger')
        elif 'signup' in request.form:
            # Handle signup
            control = UserSignupBoundary()
            control_obj = UserSignupControl()
            username = request.form['signup_username']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            address = request.form.get('address', None)
            location = request.form.get('location', None)
            if password != confirm_password:
                flash('Passwords do not match!', 'danger')
            else:
                success = control_obj.signup(username, email, password, address, location)
                if success:
                    flash('Signup successful! Please log in.', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Signup failed. Please try again.', 'danger')

    return render_template('home.html', logged_in=logged_in, username=session.get('username'))

# Route for Viewing Latest Weather (accessible without login)
@app.route('/weather', methods=['GET', 'POST'])
def view_weather():
    control = WeatherBoundary()
    control_obj = WeatherControl()

    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            try:
                weather_data = control_obj.get_latest_weather(location)
                if not weather_data:
                    flash(f'No weather data found for {location}.', 'danger')
                    weather_data = None
            except Exception as e:
                flash(f"An error occurred: {e}", 'danger')
                weather_data = None
        else:
            flash('Please enter a valid location.', 'danger')
            weather_data = None
        return render_template('weather.html', weather=weather_data, location=location)

    return render_template('weather.html')

# Route for Today's Forecast
@app.route('/today_forecast', methods=['GET'])
def view_today_forecast():
    location = request.args.get('location', 'New York')
    control = TodayForecastBoundary()
    control_obj = TodayForecastControl()
    forecast_data = control_obj.get_today_forecast(location)
    return render_template('today_forecast.html', forecast=forecast_data, location=location)

# Route for Extended Forecast
@app.route('/extended_forecast', methods=['GET'])
def view_extended_forecast():
    location = request.args.get('location', 'New York')
    days = request.args.get('days', 7, type=int)
    control = ExtendedForecastBoundary()
    control_obj = ExtendedForecastControl()
    extended_forecast_data = control_obj.get_extended_forecast(location, days)
    return render_template('extended_forecast.html', forecast=extended_forecast_data, location=location, days=days)

# Route for Viewing Historical Weather Data
@app.route('/historical_data', methods=['GET'])
def view_historical_data():
    location = request.args.get('location', 'New York')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    control = HistoricalDataBoundary()
    control_obj = HistoricalDataControl()
    historical_data = control_obj.get_historical_data(location, start_date, end_date)
    return render_template('historical_data.html', historical_data=historical_data, location=location, start_date=start_date, end_date=end_date)

# Route for FAQ
@app.route('/faq')
def faq():
    control = FAQBoundary()
    control_obj = FAQControl()
    faqs = control_obj.get_all_faqs()
    return render_template('faq.html', faqs=faqs)

# Route for Educational Content
@app.route('/educational_content')
def view_educational_content():
    topic = request.args.get('topic', 'Weather Basics')
    control = EducationalContentBoundary()
    control_obj = EducationalContentControl()
    content = control_obj.get_content_by_topic(topic)
    return render_template('educational_content.html', content=content)

# Route for Alerts and Health Advisories
@app.route('/alerts', methods=['GET', 'POST'])
def manage_alerts():
    if not session.get('username'):
        return login_required()

    control = AlertBoundary()
    control_obj = AlertControl()
    if request.method == 'POST':
        alert_type = request.form['alert_type']
        condition = request.form['condition']
        control_obj.create_user_alert(session.get('user_id'), alert_type, condition)
        flash('Alert created successfully!', 'success')

    user_location = session.get('user_location', 'New York')
    alerts = control_obj.get_user_alerts(session.get('user_id'))
    advisories = control_obj.check_health_advisory(session.get('user_id'))
    return render_template('alerts.html', alerts=alerts, advisories=advisories)

# Route for Dashboard Customization
@app.route('/customize_dashboard', methods=['GET', 'POST'])
def customize_dashboard():
    if not session.get('username'):
        return login_required()

    control = DashboardSettingsBoundary()
    control_obj = DashboardSettingsControl()
    if request.method == 'POST':
        settings = request.form.to_dict()
        control_obj.save_settings(session['user_id'], settings)
        flash('Dashboard settings saved!', 'success')
    current_settings = control_obj.load_dashboard_settings(session['user_id'])
    return render_template('dashboard.html', settings=current_settings)

# Route for Submitting Feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not session.get('username'):
        return login_required()

    control = FeedbackBoundary()
    control_obj = FeedbackControl()
    if request.method == 'POST':
        feedback_type = request.form['feedback_type']
        message = request.form['message']
        control_obj.submit_feedback(session['user_id'], feedback_type, message)
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('feedback.html')

# Route for Exporting Data
@app.route('/export', methods=['GET', 'POST'])
def export_data():
    if not session.get('username'):
        return login_required()

    control = DataExportBoundary()
    control_obj = DataExportControl()
    if request.method == 'POST':
        export_format = request.form['format']
        location = request.form['location']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        file_path = control_obj.export_data(session['user_id'], export_format, location, start_date, end_date)
        flash(f'Data exported successfully! Download at: {file_path}', 'success')
    return render_template('export.html')

# Route for Reset Password
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    control = ResetPasswordBoundary()
    control_obj = ResetPasswordControl()
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        if control_obj.reset_password(username, new_password):
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
