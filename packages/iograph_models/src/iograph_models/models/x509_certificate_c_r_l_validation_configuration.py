from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateCRLValidationConfiguration(BaseModel):
	exemptedCertificateAuthoritiesSubjectKeyIdentifiers: Optional[list[str]] = Field(alias="exemptedCertificateAuthoritiesSubjectKeyIdentifiers",default=None,)
	state: Optional[str | X509CertificateCRLValidationConfigurationState] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .x509_certificate_c_r_l_validation_configuration_state import X509CertificateCRLValidationConfigurationState

