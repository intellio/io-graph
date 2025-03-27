from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class InternalDomainFederation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.internalDomainFederation"] = Field(alias="@odata.type", default="#microsoft.graph.internalDomainFederation")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	issuerUri: Optional[str] = Field(alias="issuerUri", default=None,)
	metadataExchangeUri: Optional[str] = Field(alias="metadataExchangeUri", default=None,)
	passiveSignInUri: Optional[str] = Field(alias="passiveSignInUri", default=None,)
	preferredAuthenticationProtocol: Optional[AuthenticationProtocol | str] = Field(alias="preferredAuthenticationProtocol", default=None,)
	signingCertificate: Optional[str] = Field(alias="signingCertificate", default=None,)
	activeSignInUri: Optional[str] = Field(alias="activeSignInUri", default=None,)
	federatedIdpMfaBehavior: Optional[FederatedIdpMfaBehavior | str] = Field(alias="federatedIdpMfaBehavior", default=None,)
	isSignedAuthenticationRequestRequired: Optional[bool] = Field(alias="isSignedAuthenticationRequestRequired", default=None,)
	nextSigningCertificate: Optional[str] = Field(alias="nextSigningCertificate", default=None,)
	passwordResetUri: Optional[str] = Field(alias="passwordResetUri", default=None,)
	promptLoginBehavior: Optional[PromptLoginBehavior | str] = Field(alias="promptLoginBehavior", default=None,)
	signingCertificateUpdateStatus: Optional[SigningCertificateUpdateStatus] = Field(alias="signingCertificateUpdateStatus", default=None,)
	signOutUri: Optional[str] = Field(alias="signOutUri", default=None,)

from .authentication_protocol import AuthenticationProtocol
from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
from .prompt_login_behavior import PromptLoginBehavior
from .signing_certificate_update_status import SigningCertificateUpdateStatus

