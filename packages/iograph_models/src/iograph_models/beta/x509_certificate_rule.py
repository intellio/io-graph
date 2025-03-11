from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateRule(BaseModel):
	identifier: Optional[str] = Field(alias="identifier",default=None,)
	issuerSubjectIdentifier: Optional[str] = Field(alias="issuerSubjectIdentifier",default=None,)
	policyOidIdentifier: Optional[str] = Field(alias="policyOidIdentifier",default=None,)
	x509CertificateAuthenticationMode: Optional[X509CertificateAuthenticationMode | str] = Field(alias="x509CertificateAuthenticationMode",default=None,)
	x509CertificateRequiredAffinityLevel: Optional[X509CertificateAffinityLevel | str] = Field(alias="x509CertificateRequiredAffinityLevel",default=None,)
	x509CertificateRuleType: Optional[X509CertificateRuleType | str] = Field(alias="x509CertificateRuleType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
from .x509_certificate_affinity_level import X509CertificateAffinityLevel
from .x509_certificate_rule_type import X509CertificateRuleType

