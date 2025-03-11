from __future__ import annotations
from enum import StrEnum


class AwsAccessType(StrEnum):
	public = "public"
	restricted = "restricted"
	crossAccount = "crossAccount"
	private = "private"
	unknownFutureValue = "unknownFutureValue"

