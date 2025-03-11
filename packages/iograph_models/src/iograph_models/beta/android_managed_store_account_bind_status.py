from __future__ import annotations
from enum import StrEnum


class AndroidManagedStoreAccountBindStatus(StrEnum):
	notBound = "notBound"
	bound = "bound"
	boundAndValidated = "boundAndValidated"
	unbinding = "unbinding"

