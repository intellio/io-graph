from __future__ import annotations
from enum import StrEnum


class ExternalAuthenticationType(StrEnum):
	passthru = "passthru"
	aadPreAuthentication = "aadPreAuthentication"

