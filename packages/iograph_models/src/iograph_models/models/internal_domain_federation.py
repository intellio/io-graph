from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InternalDomainFederation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	issuerUri: Optional[str] = Field(default=None,alias="issuerUri",)
	metadataExchangeUri: Optional[str] = Field(default=None,alias="metadataExchangeUri",)
	passiveSignInUri: Optional[str] = Field(default=None,alias="passiveSignInUri",)
	preferredAuthenticationProtocol: Optional[AuthenticationProtocol] = Field(default=None,alias="preferredAuthenticationProtocol",)
	signingCertificate: Optional[str] = Field(default=None,alias="signingCertificate",)
	activeSignInUri: Optional[str] = Field(default=None,alias="activeSignInUri",)
	federatedIdpMfaBehavior: Optional[FederatedIdpMfaBehavior] = Field(default=None,alias="federatedIdpMfaBehavior",)
	isSignedAuthenticationRequestRequired: Optional[bool] = Field(default=None,alias="isSignedAuthenticationRequestRequired",)
	nextSigningCertificate: Optional[str] = Field(default=None,alias="nextSigningCertificate",)
	passwordResetUri: Optional[str] = Field(default=None,alias="passwordResetUri",)
	promptLoginBehavior: Optional[PromptLoginBehavior] = Field(default=None,alias="promptLoginBehavior",)
	signingCertificateUpdateStatus: Optional[SigningCertificateUpdateStatus] = Field(default=None,alias="signingCertificateUpdateStatus",)
	signOutUri: Optional[str] = Field(default=None,alias="signOutUri",)

from .authentication_protocol import AuthenticationProtocol
from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
from .prompt_login_behavior import PromptLoginBehavior
from .signing_certificate_update_status import SigningCertificateUpdateStatus

