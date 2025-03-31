from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class X509CertificateAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.x509CertificateAuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.x509CertificateAuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	authenticationModeConfiguration: Optional[X509CertificateAuthenticationModeConfiguration] = Field(alias="authenticationModeConfiguration", default=None,)
	certificateUserBindings: Optional[list[X509CertificateUserBinding]] = Field(alias="certificateUserBindings", default=None,)
	issuerHintsConfiguration: Optional[X509CertificateIssuerHintsConfiguration] = Field(alias="issuerHintsConfiguration", default=None,)
	includeTargets: Optional[list[Annotated[Union[MicrosoftAuthenticatorAuthenticationMethodTarget, PasskeyAuthenticationMethodTarget, SmsAuthenticationMethodTarget, VoiceAuthenticationMethodTarget],Field(discriminator="odata_type")]]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
from .x509_certificate_user_binding import X509CertificateUserBinding
from .x509_certificate_issuer_hints_configuration import X509CertificateIssuerHintsConfiguration
from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
from .sms_authentication_method_target import SmsAuthenticationMethodTarget
from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
