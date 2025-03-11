from __future__ import annotations
from enum import StrEnum


class AndroidUsernameSource(StrEnum):
	username = "username"
	userPrincipalName = "userPrincipalName"
	samAccountName = "samAccountName"
	primarySmtpAddress = "primarySmtpAddress"

