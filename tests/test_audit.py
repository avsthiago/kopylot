from kopylot.audit import (
    extract_table_from_response,
    format_table,
    json_to_dict,
    severity_color,
    sort_table,
)


def test_json_to_dict() -> None:
    assert json_to_dict("[]") == []
    assert json_to_dict('[{"key": "value"}]') == [{"key": "value"}]
    assert json_to_dict("invalid json") == []


def test_extract_table_from_response() -> None:
    assert extract_table_from_response("some string without list") == [
        {"vulnerability": "No vulnerabilities found", "severity": "n/a"}
    ]
    assert extract_table_from_response("text with [{}] list") == [{}]


def test_sort_table() -> None:
    unsorted_table = [
        {"vulnerability": "A", "severity": "HIGH"},
        {"vulnerability": "B", "severity": "LOW"},
        {"vulnerability": "C", "severity": "MEDIUM"},
    ]
    sorted_table = [
        {"vulnerability": "A", "severity": "HIGH"},
        {"vulnerability": "C", "severity": "MEDIUM"},
        {"vulnerability": "B", "severity": "LOW"},
    ]
    assert sort_table(unsorted_table) == sorted_table


def test_severity_color() -> None:
    assert severity_color("LOW", False) == "green"
    assert severity_color("MEDIUM", False) == "yellow"
    assert severity_color("HIGH", False) == "dark_orange"
    assert severity_color("CRITICAL", False) == "red1"
    assert severity_color("UNKNOWN", False) == "white"
    assert severity_color("LOW", True) == "white"


def test_create_printable_table() -> None:
    table_items = [
        {"vulnerability": "A", "severity": "HIGH"},
        {"vulnerability": "B", "severity": "LOW"},
        {"vulnerability": "C", "severity": "MEDIUM"},
    ]
    table = format_table(table_items, "Test Table")

    # print table using rich
    from rich.console import Console

    console = Console()
    console.print(table)

    assert len(table.columns) == 2
    assert len(table.rows) == 3
