from __future__ import annotations
from enum import StrEnum


class ThreatCategory(StrEnum):
	undefined = "undefined"
	spam = "spam"
	phishing = "phishing"
	malware = "malware"
	unknownFutureValue = "unknownFutureValue"

