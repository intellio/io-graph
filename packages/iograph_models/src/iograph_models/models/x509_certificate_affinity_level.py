from __future__ import annotations
from enum import Enum


class X509CertificateAffinityLevel(Enum):
	low = "low"
	high = "high"
	unknownFutureValue = "unknownFutureValue"

