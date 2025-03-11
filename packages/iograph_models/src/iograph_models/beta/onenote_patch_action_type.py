from __future__ import annotations
from enum import StrEnum


class OnenotePatchActionType(StrEnum):
	Replace = "Replace"
	Append = "Append"
	Delete = "Delete"
	Insert = "Insert"
	Prepend = "Prepend"

