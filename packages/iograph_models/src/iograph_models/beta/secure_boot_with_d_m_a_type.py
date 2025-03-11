from __future__ import annotations
from enum import StrEnum


class SecureBootWithDMAType(StrEnum):
	notConfigured = "notConfigured"
	withoutDMA = "withoutDMA"
	withDMA = "withDMA"

