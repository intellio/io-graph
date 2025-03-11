from __future__ import annotations
from enum import StrEnum


class FirewallCertificateRevocationListCheckMethodType(StrEnum):
	deviceDefault = "deviceDefault"
	none = "none"
	attempt = "attempt"
	require = "require"

