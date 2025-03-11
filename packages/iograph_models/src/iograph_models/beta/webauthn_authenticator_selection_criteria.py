from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebauthnAuthenticatorSelectionCriteria(BaseModel):
	authenticatorAttachment: Optional[str] = Field(alias="authenticatorAttachment",default=None,)
	requireResidentKey: Optional[bool] = Field(alias="requireResidentKey",default=None,)
	userVerification: Optional[str] = Field(alias="userVerification",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


