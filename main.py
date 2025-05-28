# noinspection PyUnresolvedReferences
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        print(f"🟢 Город получен: {city}")
        weather = get_weather(city)
        news = get_news()
        print(f"🟢 Новости получены: {news}")
        print(news)
    return render_template('index.html', weather=weather, news=news)

def get_weather(city):
    api_key = '92614399a18da57057e083f734235ecd'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = 'a5587f63a27e432eb1a726fcd574abc5'
    url = f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data.get('articles', [])

if __name__ == '__main__':
    app.run(debug=True)