from __future__ import annotations
from enum import StrEnum


class CloudCertificationAuthorityType(StrEnum):
	unknown = "unknown"
	rootCertificationAuthority = "rootCertificationAuthority"
	issuingCertificationAuthority = "issuingCertificationAuthority"
	issuingCertificationAuthorityWithExternalRoot = "issuingCertificationAuthorityWithExternalRoot"
	unknownFutureValue = "unknownFutureValue"

