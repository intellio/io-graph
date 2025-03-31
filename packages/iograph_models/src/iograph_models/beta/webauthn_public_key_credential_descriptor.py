from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WebauthnPublicKeyCredentialDescriptor(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	transports: Optional[list[str]] = Field(alias="transports", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

