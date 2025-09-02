
from flask import Flask, request, render_template
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)
app.jinja_env.cache = {}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# vridhi crushes snchita


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = "Delhi"

    weather_data = get_current_weather(city)
    if not str(weather_data['cod']) == "200": #here it was str or int so make it str
        return render_template('city-not-found.html')

    return render_template(f"weather.html", title=weather_data["name"], status=weather_data['weather'][0]['description'].capitalize(), temp=weather_data['main']['temp'], feels_like=f"{weather_data['main']['feels_like']:.1f}")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
