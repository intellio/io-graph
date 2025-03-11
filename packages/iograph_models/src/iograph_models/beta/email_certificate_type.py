from __future__ import annotations
from enum import StrEnum


class EmailCertificateType(StrEnum):
	none = "none"
	certificate = "certificate"
	derivedCredential = "derivedCredential"

