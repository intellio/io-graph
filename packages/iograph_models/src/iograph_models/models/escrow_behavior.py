from __future__ import annotations
from enum import Enum


class EscrowBehavior(Enum):
	Default = "Default"
	IgnoreLookupReferenceResolutionFailure = "IgnoreLookupReferenceResolutionFailure"

