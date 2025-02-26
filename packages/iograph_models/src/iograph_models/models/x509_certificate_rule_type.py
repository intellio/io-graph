from __future__ import annotations
from enum import Enum


class X509CertificateRuleType(Enum):
	issuerSubject = "issuerSubject"
	policyOID = "policyOID"
	unknownFutureValue = "unknownFutureValue"
	issuerSubjectAndPolicyOID = "issuerSubjectAndPolicyOID"

