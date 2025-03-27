from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebauthnPublicKeyCredential(BaseModel):
	clientExtensionResults: Optional[WebauthnAuthenticationExtensionsClientOutputs] = Field(alias="clientExtensionResults", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	response: Optional[WebauthnAuthenticatorAttestationResponse] = Field(alias="response", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .webauthn_authentication_extensions_client_outputs import WebauthnAuthenticationExtensionsClientOutputs
from .webauthn_authenticator_attestation_response import WebauthnAuthenticatorAttestationResponse

