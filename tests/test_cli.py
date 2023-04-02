from typing import Any
from unittest.mock import MagicMock

import pytest

from kopylot.cli import audit, ctl, diagnose


@pytest.fixture
def mock_subprocess_run(mocker: MagicMock) -> Any:
    return mocker.patch("subprocess.run")


def test_ctl(mock_subprocess_run: MagicMock) -> None:
    args = ["get", "pods"]
    ctl(args)
    mock_subprocess_run.assert_called_with("kubectl get pods", shell=True)


def test_diagnose(mock_subprocess_run: Any, mocker: MagicMock) -> None:
    mock_subprocess_run.return_value.stdout.decode = lambda _: "test yaml output"
    resource_type = "pod"
    resource_name = "test-pod"

    # Mock the llm.ask_llm function to return a pre-defined chat result
    mocker.patch("kopylot.llm.ask_llm", return_value="foo")
    diagnose(resource_type, resource_name)

    mock_subprocess_run.assert_called_with(
        f"kubectl describe {resource_type} {resource_name}", shell=True, capture_output=True
    )


def test_audit(mock_subprocess_run: Any, mocker: MagicMock) -> None:
    mock_subprocess_run.return_value.stdout.decode = lambda _: "test yaml output"
    resource_type = "pod"
    resource_name = "test-pod"

    # Mock the llm.ask_llm function to return a pre-defined chat result
    mocker.patch("kopylot.llm.ask_llm", return_value="foo")

    audit(resource_type, resource_name)

    mock_subprocess_run.assert_called_with(
        f"kubectl get {resource_type} {resource_name} -oyaml", shell=True, capture_output=True
    )
