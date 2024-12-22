# Weather Visualization App

This project is a web application built using Dash and Plotly to visualize weather data. It provides interactive graphs for temperature, wind speed, and precipitation probability, allowing users to explore weather patterns and make informed decisions based on the data.

## Project Structure

```
weather-visualization-app
├── src
│   ├── app.py                  # Main entry point for the Dash application
│   ├── data
│   │   └── weather_data.py     # Functions to fetch and preprocess weather data
│   ├── components
│   │   ├── temperature_graph.py # Interactive graph for temperature data
│   │   ├── wind_speed_graph.py  # Interactive graph for wind speed data
│   │   └── precipitation_graph.py# Interactive graph for precipitation probability
│   └── assets
│       └── styles.css          # Custom styles for the Dash application
├── requirements.txt            # List of dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather-visualization-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:8050` to view the application.

## Features

- **Temperature Graph**: Visualizes temperature data with options to select different time intervals and metrics.
- **Wind Speed Graph**: Displays wind speed data with filtering options for better analysis.
- **Precipitation Probability Graph**: Shows precipitation probability with user controls for selecting time frames and types of data.

## Usage Guidelines

- Use the dropdowns and input fields to customize the data displayed in the graphs.
- Interact with the graphs to gain insights into weather trends and patterns.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.