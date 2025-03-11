from __future__ import annotations
from enum import StrEnum


class AwsRoleTrustEntityType(StrEnum):
	none = "none"
	service = "service"
	sso = "sso"
	crossAccount = "crossAccount"
	webIdentity = "webIdentity"
	unknownFutureValue = "unknownFutureValue"

