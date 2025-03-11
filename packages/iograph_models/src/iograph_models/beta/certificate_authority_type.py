from __future__ import annotations
from enum import StrEnum


class CertificateAuthorityType(StrEnum):
	root = "root"
	intermediate = "intermediate"
	unknownFutureValue = "unknownFutureValue"

