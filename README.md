# ForecastForge
ForecastForge: Your weather companion crafting precision forecasts. With real-time updates, interactive maps, and personalized history, navigate meteorological insights effortlessly. Experience weather, redefined

# Weather Forecasting Django WebApp

## Overview

This Django web application provides weather forecasting based on the OpenWeatherMap API. Users can search for weather information for a specific location and view a 7-day weather forecast.

## Features

- Current weather information
- 7-day weather forecast
- Dynamic background color based on weather conditions
- Responsive design for different devices

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/SHIV000000/ForecastForge.git
```
### Change into the project directory:

```bash
cd weather forecast
```

### Create and activate a virtual environment:

# On Macos\Linux:
```bash
python3 -m venv venv
 ```
```bash
source venv/bin/activate
```
# On Windows:
```bash
py -m venv venv
```

```bash
venv\Scripts\activate
```

## Install the required dependencies:

 ```bash
pip install -r requirements.txt
```

### Configure API Key:

Get your OpenWeatherMap API key from OpenWeatherMap.
Update the API_KEY in the credentials.py file.

### Run migrations:

```bash
python manage.py makemigration
python manage.py migrate
```

### Run the development server:

```bash
python manage.py runserver
```

Open your browser and visit http://127.0.0.1:8000/ to access the application.

###Configuration

Update the SECRET_KEY in settings.py with your Django project secret key.
Adjust other settings in settings.py as needed.

Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix:

```bash
git checkout -b feature-name
```
### Commit your changes:

```bash
git commit -m 'Add new feature'
```

###Push to the branch:

```bash
git push origin feature-name
```
Submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
