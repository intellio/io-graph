from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateCRLValidationConfiguration(BaseModel):
	exemptedCertificateAuthoritiesSubjectKeyIdentifiers: list[Optional[str]] = Field(alias="exemptedCertificateAuthoritiesSubjectKeyIdentifiers",)
	state: Optional[X509CertificateCRLValidationConfigurationState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .x509_certificate_c_r_l_validation_configuration_state import X509CertificateCRLValidationConfigurationState

