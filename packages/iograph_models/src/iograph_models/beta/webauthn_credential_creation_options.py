from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WebauthnCredentialCreationOptions(BaseModel):
	challengeTimeoutDateTime: Optional[datetime] = Field(alias="challengeTimeoutDateTime", default=None,)
	publicKey: Optional[WebauthnPublicKeyCredentialCreationOptions] = Field(alias="publicKey", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .webauthn_public_key_credential_creation_options import WebauthnPublicKeyCredentialCreationOptions

