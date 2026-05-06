import requests


def github_repo_tool(owner: str, repo: str) -> str:
    """
    GitHub 仓库查询工具：输入 owner 和 repo，返回仓库基本信息。
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code != 200:
        return f"查询失败，状态码：{response.status_code}"

    data = response.json()

    name = data.get("full_name")
    description = data.get("description")
    stars = data.get("stargazers_count")
    forks = data.get("forks_count")
    language = data.get("language")
    html_url = data.get("html_url")

    return (
        f"仓库名称：{name}\n"
        f"项目简介：{description}\n"
        f"Star 数：{stars}\n"
        f"Fork 数：{forks}\n"
        f"主要语言：{language}\n"
        f"仓库地址：{html_url}"
    )