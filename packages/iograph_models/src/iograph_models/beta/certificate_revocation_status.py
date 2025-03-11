from __future__ import annotations
from enum import StrEnum


class CertificateRevocationStatus(StrEnum):
	none = "none"
	pending = "pending"
	issued = "issued"
	failed = "failed"
	revoked = "revoked"

