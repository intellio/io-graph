from __future__ import annotations
from enum import StrEnum


class BitLockerRecoveryInformationType(StrEnum):
	passwordAndKey = "passwordAndKey"
	passwordOnly = "passwordOnly"

