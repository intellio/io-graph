from __future__ import annotations
from enum import Enum


class ThreatCategory(Enum):
	undefined = "undefined"
	spam = "spam"
	phishing = "phishing"
	malware = "malware"
	unknownFutureValue = "unknownFutureValue"

