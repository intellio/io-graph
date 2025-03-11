from __future__ import annotations
from enum import StrEnum


class GcpEncryption(StrEnum):
	google = "google"
	customer = "customer"
	unknownFutureValue = "unknownFutureValue"

