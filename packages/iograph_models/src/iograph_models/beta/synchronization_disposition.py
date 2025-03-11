from __future__ import annotations
from enum import StrEnum


class SynchronizationDisposition(StrEnum):
	Normal = "Normal"
	Discard = "Discard"
	Escrow = "Escrow"

