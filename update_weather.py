import requests
from datetime import datetime

# Use wttr.in API (no API key needed)
city = "Hyderabad"
url = f"https://wttr.in/{city}?format=j1"

print(f"Fetching weather data for {city}...")
try:
    response = requests.get(url, timeout=10)
    data = response.json()
    
    # Extract weather information
    current = data['current_condition'][0]
    astronomy = data['weather'][0]['astronomy'][0]
    
    weather_desc = current['weatherDesc'][0]['value']
    temp = f"{current['temp_C']}°C"
    humidity = f"{current['humidity']}%"
    sunrise_ist = astronomy['sunrise']
    sunset_ist = astronomy['sunset']
    
    # Map weather description to icon code
    weather_code = int(current['weatherCode'])
    if weather_code == 113:
        icon_code = "01d"  # Clear/Sunny
    elif weather_code in [116, 119]:
        icon_code = "02d"  # Partly cloudy
    elif weather_code in [122, 143, 248, 260]:
        icon_code = "03d"  # Cloudy/Overcast
    elif weather_code in [176, 263, 266, 293, 296]:
        icon_code = "09d"  # Light rain
    elif weather_code in [299, 302, 305, 308, 311, 314, 317, 320, 353, 356, 359]:
        icon_code = "10d"  # Rain
    elif weather_code in [200, 386, 389, 392, 395]:
        icon_code = "11d"  # Thunderstorm
    elif weather_code in [227, 230, 323, 326, 329, 332, 335, 338, 350, 362, 365, 368, 371, 374, 377]:
        icon_code = "13d"  # Snow
    else:
        icon_code = "50d"  # Mist/Fog
    
    print(f"\nWeather: {weather_desc}")
    print(f"Temperature: {temp}")
    print(f"Sunrise: {sunrise_ist}")
    print(f"Sunset: {sunset_ist}")
    print(f"Humidity: {humidity}")
    
except Exception as e:
    print(f"Error fetching weather: {e}")
    print("Using sample data...")
    weather_desc = "Clear Sky"
    temp = "25°C"
    humidity = "60%"
    sunrise_ist = "06:30 AM"
    sunset_ist = "06:00 PM"
    icon_code = "01d"

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Create weather table
weather_table = f'''<!-- Hyderabad's weather table -->

<h2 align="center"> 🇮🇳 Hyderabad's Weather ⛅ </h2>
<table align="center" style="width:50%">
    <tr style="text-align:center">
        <th>Weather</th>
        <th>Temperature</th>
        <th>Sunrise</th>
        <th>Sunset</th>
        <th>Humidity</th>
    </tr>
    <tr style="text-align:center">
        <td><b>{weather_desc}</b> <img width="20" src="http://openweathermap.org/img/w/{icon_code}.png"></td>
        <td><b>{temp}</b></td>
        <td><b>{sunrise_ist}</b></td>
        <td><b>{sunset_ist}</b></td>
        <td><b>{humidity}</b></td>
    </tr>
</table>'''

# Replace weather section
start_marker = "<!-- Hyderabad's weather table -->"
end_marker = "</table>"

start_idx = readme.find(start_marker)
if start_idx != -1:
    end_idx = readme.find(end_marker, start_idx) + len(end_marker)
    readme = readme[:start_idx] + weather_table + readme[end_idx:]
    
    # Write updated README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print("\n✅ README.md updated successfully!")
    print("Now run: git commit -a -m '🌤️ Update weather data' && git push")
else:
    print("\n❌ Could not find weather table marker in README.md")
