CREATE DATABASE weather_website;
USE weather_website;

-- Table for users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    location VARCHAR(100),
    password_hash VARCHAR(255) NOT NULL
);

-- Table for weather data
CREATE TABLE weather_data (
    weather_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100),
    temperature FLOAT,
    humidity FLOAT,users
    wind_speed FLOAT,
    conditions VARCHAR(100),
    date DATE
);

-- Table for alerts
CREATE TABLE alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    alert_type VARCHAR(100),
    conditions VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table for feedback
CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    username VARCHAR(100),
    feedback_type VARCHAR(100),
    message TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table for health advisories
CREATE TABLE health_advisories (
    advisory_id INT AUTO_INCREMENT PRIMARY KEY,
    conditions VARCHAR(100),
    message TEXT
);

-- Table for dashboard settings
CREATE TABLE dashboard_settings (
    user_id INT PRIMARY KEY,
    settings TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table for data exports
CREATE TABLE data_exports (
    export_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    export_path VARCHAR(255),
    export_format VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

USE weather_website;
CREATE TABLE IF NOT EXISTS faqs (
            FAQID INT AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(255) NOT NULL,
            answer TEXT NOT NULL
        );

USE weather_website;
INSERT INTO faqs (question, answer) VALUES 
        ('What is the weather app?', 'The weather app provides real-time weather information for various locations.'),
        ('How do I create an alert?', 'You can create an alert by navigating to the alerts section and filling out the alert form.'),
        ('Can I customize my dashboard?', 'Yes, you can customize your dashboard');
	
USE weather_website;
CREATE TABLE educational_content  (
    contentID INT AUTO_INCREMENT PRIMARY KEY,
    contentType VARCHAR(32),
    contentURL VARCHAR(255)
);    
    
#USE weather_website;
INSERT INTO educational_content (question, answer) VALUES 
        ('What is the weather app?', 'The weather app provides real-time weather information for various locations.'),
        ('How do I create an alert?', 'You can create an alert by navigating to the alerts section and filling out the alert form.'),
        ('Can I customize my dashboard?', 'Yes, you can customize your dashboard');       


