from __future__ import annotations
from enum import StrEnum


class UserEmailSource(StrEnum):
	userPrincipalName = "userPrincipalName"
	primarySmtpAddress = "primarySmtpAddress"

