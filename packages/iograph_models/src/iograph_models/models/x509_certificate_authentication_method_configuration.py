from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: list[ExcludeTarget] = Field(alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	authenticationModeConfiguration: Optional[X509CertificateAuthenticationModeConfiguration] = Field(default=None,alias="authenticationModeConfiguration",)
	certificateUserBindings: list[X509CertificateUserBinding] = Field(alias="certificateUserBindings",)
	crlValidationConfiguration: Optional[X509CertificateCRLValidationConfiguration] = Field(default=None,alias="crlValidationConfiguration",)
	includeTargets: list[AuthenticationMethodTarget] = Field(alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
from .x509_certificate_user_binding import X509CertificateUserBinding
from .x509_certificate_c_r_l_validation_configuration import X509CertificateCRLValidationConfiguration
from .authentication_method_target import AuthenticationMethodTarget

