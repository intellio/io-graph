from __future__ import annotations
from enum import StrEnum


class CertificateDestinationStore(StrEnum):
	computerCertStoreRoot = "computerCertStoreRoot"
	computerCertStoreIntermediate = "computerCertStoreIntermediate"
	userCertStoreIntermediate = "userCertStoreIntermediate"

