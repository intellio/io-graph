from __future__ import annotations
from enum import StrEnum


class VpnLocalIdentifier(StrEnum):
	deviceFQDN = "deviceFQDN"
	empty = "empty"
	clientCertificateSubjectName = "clientCertificateSubjectName"

