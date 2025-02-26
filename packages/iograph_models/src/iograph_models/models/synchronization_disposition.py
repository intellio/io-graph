from __future__ import annotations
from enum import Enum


class SynchronizationDisposition(Enum):
	Normal = "Normal"
	Discard = "Discard"
	Escrow = "Escrow"

