from __future__ import annotations
from enum import StrEnum


class AndroidEapType(StrEnum):
	eapTls = "eapTls"
	eapTtls = "eapTtls"
	peap = "peap"

