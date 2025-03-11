from __future__ import annotations
from enum import StrEnum


class SharedPCAllowedAccountType(StrEnum):
	notConfigured = "notConfigured"
	guest = "guest"
	domain = "domain"

