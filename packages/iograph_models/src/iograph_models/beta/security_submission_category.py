from __future__ import annotations
from enum import StrEnum


class SecuritySubmissionCategory(StrEnum):
	notJunk = "notJunk"
	spam = "spam"
	phishing = "phishing"
	malware = "malware"
	unknownFutureValue = "unknownFutureValue"

