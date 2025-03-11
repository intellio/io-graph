from __future__ import annotations
from enum import StrEnum


class AuthorizationSystemType(StrEnum):
	azure = "azure"
	gcp = "gcp"
	aws = "aws"
	unknownFutureValue = "unknownFutureValue"

