from __future__ import annotations
from enum import StrEnum


class UsernameSource(StrEnum):
	userPrincipalName = "userPrincipalName"
	primarySmtpAddress = "primarySmtpAddress"
	samAccountName = "samAccountName"

