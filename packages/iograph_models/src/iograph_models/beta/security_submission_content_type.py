from __future__ import annotations
from enum import StrEnum


class SecuritySubmissionContentType(StrEnum):
	email = "email"
	url = "url"
	file = "file"
	app = "app"
	unknownFutureValue = "unknownFutureValue"

