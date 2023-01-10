from typing import List, Dict


def clear_chat_gpt_message(text: str) -> str:
    """
    Remove extra symbols from message
    """
    if text.startswith("?"):
        text = text.strip("?")
    return text.strip("\n")


def chat_gpt_response_to_text(
    response: List[Dict[str, str]]
) -> str:
    """
    Transformation chat GPT response to text
    """
    result = []
    for message in response:
        clear_message = clear_chat_gpt_message(
            message.get("text")
        )
        result.append(clear_message)
    return " ".join(result)
