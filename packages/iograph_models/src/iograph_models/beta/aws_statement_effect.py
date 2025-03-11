from __future__ import annotations
from enum import StrEnum


class AwsStatementEffect(StrEnum):
	allow = "allow"
	deny = "deny"
	unknownFutureValue = "unknownFutureValue"

