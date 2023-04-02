from kopylot import llm, prompts


def extract_command(chat_result: str) -> str:
    if "Command: " in chat_result:
        return chat_result.split("Command: ")[1]
    else:
        return chat_result


def run_chat(user_prompt: str) -> str:
    prompt = prompts.kubectl_command_prompt(task_description=user_prompt)
    command = extract_command(llm.ask_llm(prompt))
    return command
