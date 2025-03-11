from __future__ import annotations
from enum import StrEnum


class BitLockerEncryptionMethod(StrEnum):
	aesCbc128 = "aesCbc128"
	aesCbc256 = "aesCbc256"
	xtsAes128 = "xtsAes128"
	xtsAes256 = "xtsAes256"

