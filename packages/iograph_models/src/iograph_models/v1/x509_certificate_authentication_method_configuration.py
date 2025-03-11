from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets",default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state",default=None,)
	authenticationModeConfiguration: Optional[X509CertificateAuthenticationModeConfiguration] = Field(alias="authenticationModeConfiguration",default=None,)
	certificateUserBindings: Optional[list[X509CertificateUserBinding]] = Field(alias="certificateUserBindings",default=None,)
	crlValidationConfiguration: Optional[X509CertificateCRLValidationConfiguration] = Field(alias="crlValidationConfiguration",default=None,)
	includeTargets: SerializeAsAny[Optional[list[AuthenticationMethodTarget]]] = Field(alias="includeTargets",default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
from .x509_certificate_user_binding import X509CertificateUserBinding
from .x509_certificate_c_r_l_validation_configuration import X509CertificateCRLValidationConfiguration
from .authentication_method_target import AuthenticationMethodTarget

