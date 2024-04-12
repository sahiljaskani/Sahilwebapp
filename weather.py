from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_temperature(latitude, longitude):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    headers = {'User-Agent': 'SkoleOppgave/1.0 myemail@example.com'}
    params = {'lat': latitude, 'lon': longitude}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        try:
            first_timeseries_entry = data['properties']['timeseries'][0]
            temperature = first_timeseries_entry['data']['instant']['details']['air_temperature']
            return temperature
        except (KeyError, IndexError):
            return "Temperature data not available"
    else:
        return "Failed to fetch data"   

@app.route('/')
def home():
    latitude = 60.16804  # Example latitude
    longitude = 10.25647  # Example longitude
    temperature = fetch_temperature(latitude, longitude)
    return render_template('index.html', temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)
