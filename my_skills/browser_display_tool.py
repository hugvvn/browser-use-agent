async def run_browser_use(user_task: str):
    """
    使用 browser-use Agent 执行通用浏览器任务
    """

    llm = ChatOpenAI(
        model="你的模型",
        api_key="你的API_KEY",
        base_url="****"
    )

    # 这里先手动把中文任务改成英文提示，避免 browser-use 编码问题
    safe_task = f"""
    Please complete the following browser automation task.
    If the user's task is in Chinese, understand it and execute it correctly.

    User task:
    {user_task}
    """

    agent = Agent(
        task=safe_task,
        llm=llm,
    )

    history = await agent.run()
    return history.final_result()