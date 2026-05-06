from my_skills.weather_skill import query_weather


def weather_tool(city: str) -> str:
    """
    天气查询工具：输入城市名称，返回当前天气信息。
    """
    result = query_weather(city)
    return result