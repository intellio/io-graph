from __future__ import annotations
from enum import StrEnum


class UserPfxIntendedPurpose(StrEnum):
	unassigned = "unassigned"
	smimeEncryption = "smimeEncryption"
	smimeSigning = "smimeSigning"
	vpn = "vpn"
	wifi = "wifi"

