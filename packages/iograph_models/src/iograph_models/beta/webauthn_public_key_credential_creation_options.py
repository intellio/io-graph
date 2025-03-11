from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebauthnPublicKeyCredentialCreationOptions(BaseModel):
	attestation: Optional[str] = Field(alias="attestation",default=None,)
	authenticatorSelection: Optional[WebauthnAuthenticatorSelectionCriteria] = Field(alias="authenticatorSelection",default=None,)
	challenge: Optional[str] = Field(alias="challenge",default=None,)
	excludeCredentials: Optional[list[WebauthnPublicKeyCredentialDescriptor]] = Field(alias="excludeCredentials",default=None,)
	extensions: Optional[WebauthnAuthenticationExtensionsClientInputs] = Field(alias="extensions",default=None,)
	pubKeyCredParams: Optional[list[WebauthnPublicKeyCredentialParameters]] = Field(alias="pubKeyCredParams",default=None,)
	rp: Optional[WebauthnPublicKeyCredentialRpEntity] = Field(alias="rp",default=None,)
	timeout: Optional[int] = Field(alias="timeout",default=None,)
	user: Optional[WebauthnPublicKeyCredentialUserEntity] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .webauthn_authenticator_selection_criteria import WebauthnAuthenticatorSelectionCriteria
from .webauthn_public_key_credential_descriptor import WebauthnPublicKeyCredentialDescriptor
from .webauthn_authentication_extensions_client_inputs import WebauthnAuthenticationExtensionsClientInputs
from .webauthn_public_key_credential_parameters import WebauthnPublicKeyCredentialParameters
from .webauthn_public_key_credential_rp_entity import WebauthnPublicKeyCredentialRpEntity
from .webauthn_public_key_credential_user_entity import WebauthnPublicKeyCredentialUserEntity

