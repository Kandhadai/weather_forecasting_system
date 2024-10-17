from flask import Flask, render_template, request, redirect, url_for, flash, session
from controls.user_login_control import UserLoginControl
from controls.weather_control import ViewWeatherControl
from controls.feedback_control import FeedbackControl
from controls.dashboard_settings_control import CustomizeDashboardControl
from controls.alert_control import AlertControl
from controls.data_Export_control import ExportDataControl
from controls.educational_content_control import ViewEducationalContentControl

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Use a secure key in production


# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Route for User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    control = UserLoginControl()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if control.authenticate(username, password):
            session['username'] = username
            session['user_id'] = control.get_user_id(username)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')


# Route for Reset Password
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    control = UserLoginControl()
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        if control.reset_password(username, new_password):
            flash('Password reset successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error resetting password', 'danger')
    return render_template('reset_password.html')


# Route for Viewing Latest Weather
@app.route('/weather', methods=['GET'])
def view_weather():
    location = request.args.get('location', 'Default Location')
    control = ViewWeatherControl()
    weather_data = control.get_latest_weather(location)
    if not weather_data:
        flash('No weather data found for the selected location.', 'danger')
    return render_template('weather.html', weather=weather_data)


# Route for Viewing Today’s Forecast
@app.route('/today_forecast', methods=['GET'])
def view_today_forecast():
    location = request.args.get('location', 'Default Location')
    control = ViewWeatherControl()
    forecast_data = control.get_today_forecast(location)
    return render_template('today_forecast.html', forecast=forecast_data)


# Route for Viewing Extended Forecast
@app.route('/extended_forecast', methods=['GET'])
def view_extended_forecast():
    location = request.args.get('location', 'Default Location')
    days = request.args.get('days', 7, type=int)
    control = ViewWeatherControl()
    forecast_data = control.get_extended_forecast(location, days)
    return render_template('extended_forecast.html', forecast=forecast_data)


# Route for Viewing Historical Weather Data
@app.route('/historical_data', methods=['GET'])
def view_historical_data():
    location = request.args.get('location', 'Default Location')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    control = ViewWeatherControl()
    historical_data = control.get_historical_data(location, start_date, end_date)
    return render_template('historical_data.html', historical_data=historical_data)


# Route for Alerts and Health Advisories
@app.route('/alerts', methods=['GET', 'POST'])
def manage_alerts():
    control = AlertControl()
    if request.method == 'POST':
        alert_type = request.form['alert_type']
        condition = request.form['condition']
        control.create_user_alert(session.get('user_id'), alert_type, condition)
        flash('Alert created successfully!', 'success')

    # Assuming the user location is stored in the session
    user_location = session.get('user_location',
                                'Default Location')  # Replace 'Default Location' with an actual fallback location if needed

    alerts = control.get_user_alerts(session.get('user_id'))
    advisories = control.check_health_advisories(session.get('user_id'), user_location)
    return render_template('alerts.html', alerts=alerts, advisories=advisories)


# Route for Dashboard Customization
@app.route('/customize_dashboard', methods=['GET', 'POST'])
def customize_dashboard():
    control = CustomizeDashboardControl()
    if request.method == 'POST':
        settings = request.form.to_dict()
        control.save_settings(session['user_id'], settings)
        flash('Dashboard settings saved!', 'success')
    current_settings = control.load_dashboard_settings(session['user_id'])
    return render_template('dashboard.html', settings=current_settings)


# Route for Submitting Feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    control = FeedbackControl()
    if request.method == 'POST':
        feedback_type = request.form['feedback_type']
        message = request.form['message']
        control.submit_feedback(session['user_id'], session['username'], feedback_type, message)
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('feedback.html')


# Route for Exporting Data
@app.route('/export', methods=['GET', 'POST'])
def export_data():
    control = ExportDataControl()
    if request.method == 'POST':
        export_format = request.form['format']
        location = request.form['location']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        file_path = control.export_data(session['user_id'], export_format, location, start_date, end_date)
        flash(f'Data exported successfully! Download at: {file_path}', 'success')
    return render_template('export.html')


# Route for Viewing Educational Content
@app.route('/educational_content')
def view_educational_content():
    topic = request.args.get('topic', 'Weather Basics')
    control = ViewEducationalContentControl()
    content = control.get_content_by_topic(topic)
    return render_template('educational_content.html', content=content)


if __name__ == '__main__':
    app.run(debug=True)
