# -*- coding: utf-8 -*-

import sys
import io
import asyncio

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from browser_use import Agent
from browser_use.llm import ChatOpenAI
from my_skills.weather_tool import weather_tool
from my_skills.github_tool import github_repo_tool


def skill_router(user_task: str):
    """
    判断是否应该优先调用自定义 skill
    返回：
    - 如果命中 skill：返回结果字符串
    - 如果没有命中：返回 None，交给 browser-use
    """

    # 1. 天气查询：优先走 Weather API
    if "天气" in user_task or "weather" in user_task.lower():
        city = input("请输入城市：")
        result = weather_tool(city)
        return result

    # 2. GitHub 查询：优先走 GitHub API
    if "github" in user_task.lower():
        repo_text = input("请输入 GitHub 仓库，例如 browser-use/browser-use：")

        if "/" not in repo_text:
            return "格式错误，请输入类似 browser-use/browser-use 的格式"

        owner, repo = repo_text.split("/", 1)
        result = github_repo_tool(owner, repo)
        return result

    # 3. 没有匹配到 skill，交给 browser-use
    return None


async def run_browser_use(user_task: str):
    """
    使用 browser-use Agent 执行通用浏览器任务
    """

    llm = ChatOpenAI(
        model="你的模型",
        api_key="你的api",
        base_url="..."
    )

    agent = Agent(
        task=user_task,
        llm=llm,
    )

    history = await agent.run()
    return history.final_result()


async def main():
    user_task = input("请输入任务：")

    # 1. 先尝试调用自定义 skill
    skill_result = skill_router(user_task)

    if skill_result is not None:
        print("\n===== Skill 查询结果 =====")
        print(skill_result)
        return

    # 2. 如果没有合适的 skill，再交给 browser-use
    print("\n未命中自定义 Skill，交给 browser-use Agent 执行...\n")

    result = await run_browser_use(user_task)

    print("\n===== browser-use 执行结果 =====")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())