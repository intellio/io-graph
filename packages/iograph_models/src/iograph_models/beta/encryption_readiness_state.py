from __future__ import annotations
from enum import StrEnum


class EncryptionReadinessState(StrEnum):
	notReady = "notReady"
	ready = "ready"

