from __future__ import annotations
from enum import Enum


class OnenotePatchActionType(Enum):
	Replace = "Replace"
	Append = "Append"
	Delete = "Delete"
	Insert = "Insert"
	Prepend = "Prepend"

