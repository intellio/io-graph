from __future__ import annotations
from enum import StrEnum


class EscrowBehavior(StrEnum):
	Default = "Default"
	IgnoreLookupReferenceResolutionFailure = "IgnoreLookupReferenceResolutionFailure"

