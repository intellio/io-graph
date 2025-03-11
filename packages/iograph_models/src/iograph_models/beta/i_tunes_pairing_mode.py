from __future__ import annotations
from enum import StrEnum


class ITunesPairingMode(StrEnum):
	disallow = "disallow"
	allow = "allow"
	requiresCertificate = "requiresCertificate"

