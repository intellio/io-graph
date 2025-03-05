from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateAuthenticationModeConfiguration(BaseModel):
	rules: Optional[list[X509CertificateRule]] = Field(default=None,alias="rules",)
	x509CertificateAuthenticationDefaultMode: Optional[X509CertificateAuthenticationMode] = Field(default=None,alias="x509CertificateAuthenticationDefaultMode",)
	x509CertificateDefaultRequiredAffinityLevel: Optional[X509CertificateAffinityLevel] = Field(default=None,alias="x509CertificateDefaultRequiredAffinityLevel",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .x509_certificate_rule import X509CertificateRule
from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
from .x509_certificate_affinity_level import X509CertificateAffinityLevel

