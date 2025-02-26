from __future__ import annotations
from enum import Enum


class EntrySyncOperation(Enum):
	None_ = "None_"
	Add = "Add"
	Delete = "Delete"
	Update = "Update"

