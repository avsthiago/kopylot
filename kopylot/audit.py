import json
import re
from typing import Dict, List

from rich.table import Table

from kopylot import llm, prompts

ListDict = List[Dict[str, str]]


def json_to_dict(json_str: str) -> ListDict:
    try:
        json_loaded: List = json.loads(json_str)
    except json.JSONDecodeError:
        return []
    else:
        return json_loaded


def extract_table_from_response(s: str) -> ListDict:
    match = re.search(r"\[([^]]+)\]", s)
    extracted_table: ListDict = [{"vulnerability": "No vulnerabilities found", "severity": "n/a"}]
    if match:
        json_list_str = match.group(0)
        extracted_table = json_to_dict(json_list_str)
    return extracted_table


def sort_table(table: ListDict) -> ListDict:
    def sort_key(vulnerability: Dict[str, str]) -> int:
        severity_map = {"n/a": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
        return severity_map[vulnerability["severity"]]

    return sorted(table, key=sort_key, reverse=True)


def severity_color(severity: str, no_color: bool) -> str:
    if no_color:
        return "white"

    color_map = {
        "LOW": "green",
        "MEDIUM": "yellow",
        "HIGH": "dark_orange",
        "CRITICAL": "red1",
    }

    return color_map.get(severity, "white")


def format_table(table_tems: ListDict, title: str, no_color: bool = False) -> Table:
    table = Table(title=title, show_header=True, header_style="bold magenta", show_lines=True, title_style="bold")
    table.add_column("Vulnerability", justify="left", style="", no_wrap=True)
    table.add_column("Severity", justify="center", style="bold")

    for item in table_tems:
        vulnerability = item.get("vulnerability", "n/a")
        severity = item.get("severity", "n/a")
        color = severity_color(severity, no_color)

        table.add_row(vulnerability, f"[{color}]{severity}")
    return table


def create_printtable_table(response: str, title: str, no_color: bool) -> Table:
    table = extract_table_from_response(response)
    sorted_table = sort_table(table)
    return format_table(sorted_table, title, no_color)


def run_audit(resource_type: str, resource_yaml: str) -> str:
    prompt = prompts.audit_prompt(resource_type, resource_yaml)
    response = llm.ask_llm(prompt)
    return response
