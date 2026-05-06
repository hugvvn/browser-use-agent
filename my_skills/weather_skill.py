
import requests


def query_weather(city: str):
    api_key = "天气api"

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        f"?q={city}"
        f"&appid={api_key}"
        f"&units=metric"
        f"&lang=zh_cn"
    )

    response = requests.get(url)
    data = response.json()

    print("状态码：", response.status_code)
    print("返回内容：", data)

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"{city} 当前天气：{weather}，温度：{temperature}℃"
    else:
        return f"Failed to retrieve weather data. 原因：{data}"