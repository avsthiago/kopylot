import pytest_mock

from kopylot.chat import extract_command, run_chat


def test_extract_command() -> None:
    chat_result = "Command: kubectl get pods"
    expected_command = "kubectl get pods"
    assert extract_command(chat_result) == expected_command


def test_run_chat(mocker: pytest_mock.plugin.MockerFixture) -> None:
    user_prompt = "Show the status of all pods running in the 'production' namespace:"
    expected_command = "kubectl get pods -n production"

    # Mock the llm.ask_llm function to return a pre-defined chat result
    mocker.patch("kopylot.llm.ask_llm", return_value=f"Command: {expected_command}")

    command = run_chat(user_prompt)
    assert command == expected_command
