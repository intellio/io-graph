from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateAuthenticationModeConfiguration(BaseModel):
	rules: Optional[list[X509CertificateRule]] = Field(alias="rules", default=None,)
	x509CertificateAuthenticationDefaultMode: Optional[X509CertificateAuthenticationMode | str] = Field(alias="x509CertificateAuthenticationDefaultMode", default=None,)
	x509CertificateDefaultRequiredAffinityLevel: Optional[X509CertificateAffinityLevel | str] = Field(alias="x509CertificateDefaultRequiredAffinityLevel", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .x509_certificate_rule import X509CertificateRule
from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
from .x509_certificate_affinity_level import X509CertificateAffinityLevel
