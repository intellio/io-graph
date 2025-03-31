from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WebauthnAuthenticatorAttestationResponse(BaseModel):
	attestationObject: Optional[str] = Field(alias="attestationObject", default=None,)
	clientDataJSON: Optional[str] = Field(alias="clientDataJSON", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

