from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateRule(BaseModel):
	identifier: Optional[str] = Field(default=None,alias="identifier",)
	issuerSubjectIdentifier: Optional[str] = Field(default=None,alias="issuerSubjectIdentifier",)
	policyOidIdentifier: Optional[str] = Field(default=None,alias="policyOidIdentifier",)
	x509CertificateAuthenticationMode: Optional[X509CertificateAuthenticationMode] = Field(default=None,alias="x509CertificateAuthenticationMode",)
	x509CertificateRequiredAffinityLevel: Optional[X509CertificateAffinityLevel] = Field(default=None,alias="x509CertificateRequiredAffinityLevel",)
	x509CertificateRuleType: Optional[X509CertificateRuleType] = Field(default=None,alias="x509CertificateRuleType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
from .x509_certificate_affinity_level import X509CertificateAffinityLevel
from .x509_certificate_rule_type import X509CertificateRuleType

