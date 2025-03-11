from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebauthnPublicKeyCredentialParametersCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WebauthnPublicKeyCredentialParameters]] = Field(alias="value",default=None,)

from .webauthn_public_key_credential_parameters import WebauthnPublicKeyCredentialParameters

