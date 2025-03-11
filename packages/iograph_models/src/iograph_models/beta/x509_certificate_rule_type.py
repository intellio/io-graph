from __future__ import annotations
from enum import StrEnum


class X509CertificateRuleType(StrEnum):
	issuerSubject = "issuerSubject"
	policyOID = "policyOID"
	unknownFutureValue = "unknownFutureValue"
	issuerSubjectAndPolicyOID = "issuerSubjectAndPolicyOID"

