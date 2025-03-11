from __future__ import annotations
from enum import StrEnum


class NetworkSingleSignOnType(StrEnum):
	disabled = "disabled"
	prelogon = "prelogon"
	postlogon = "postlogon"

