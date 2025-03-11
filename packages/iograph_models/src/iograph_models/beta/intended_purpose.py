from __future__ import annotations
from enum import StrEnum


class IntendedPurpose(StrEnum):
	unassigned = "unassigned"
	smimeEncryption = "smimeEncryption"
	smimeSigning = "smimeSigning"
	vpn = "vpn"
	wifi = "wifi"

