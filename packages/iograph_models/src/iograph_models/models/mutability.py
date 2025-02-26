from __future__ import annotations
from enum import Enum


class Mutability(Enum):
	ReadWrite = "ReadWrite"
	ReadOnly = "ReadOnly"
	Immutable = "Immutable"
	WriteOnly = "WriteOnly"

