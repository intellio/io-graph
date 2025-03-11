from __future__ import annotations
from enum import StrEnum


class Mutability(StrEnum):
	ReadWrite = "ReadWrite"
	ReadOnly = "ReadOnly"
	Immutable = "Immutable"
	WriteOnly = "WriteOnly"

