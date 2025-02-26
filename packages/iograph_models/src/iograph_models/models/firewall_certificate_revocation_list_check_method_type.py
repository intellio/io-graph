from __future__ import annotations
from enum import Enum


class FirewallCertificateRevocationListCheckMethodType(Enum):
	deviceDefault = "deviceDefault"
	none = "none"
	attempt = "attempt"
	require = "require"

