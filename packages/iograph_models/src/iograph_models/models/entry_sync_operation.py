from __future__ import annotations
from enum import StrEnum


class EntrySyncOperation(StrEnum):
	None_ = "None_"
	Add = "Add"
	Delete = "Delete"
	Update = "Update"

