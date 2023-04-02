from kopylot import prompts
from kopylot.diagnose import run_diagnose


def test_run_diagnose(mocker):
    mock_ask_llm = mocker.patch("kopylot.llm.ask_llm")
    mock_ask_llm.return_value = "No errors detected"

    resource_type = "pod"
    resource_description = "Example pod description"

    result = run_diagnose(resource_type, resource_description)
    mock_ask_llm.assert_called_with(prompts.diagnose_prompt(resource_type, resource_description))
    assert result == "No errors detected"
