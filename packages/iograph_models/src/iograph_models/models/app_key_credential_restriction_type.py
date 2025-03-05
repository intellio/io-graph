from __future__ import annotations
from enum import StrEnum


class AppKeyCredentialRestrictionType(StrEnum):
	asymmetricKeyLifetime = "asymmetricKeyLifetime"
	unknownFutureValue = "unknownFutureValue"

