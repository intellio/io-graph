from __future__ import annotations
from enum import StrEnum


class AzureAccessType(StrEnum):
	public = "public"
	private = "private"
	unknownFutureValue = "unknownFutureValue"

