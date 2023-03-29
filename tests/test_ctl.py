from typing import Any
from unittest.mock import MagicMock, patch

from kopylot.cli import ctl


@patch("kopylot.cli.subprocess.run")
def test_get_data_valid(mock_run: Any) -> None:
    mock_stdout = MagicMock()
    mock_stdout.configure_mock(stdout="No resources found in default namespace.")
    mock_run.return_value = mock_stdout
    result = ctl(["get", "pods"])
    assert result.stdout == "No resources found in default namespace."
