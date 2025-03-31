from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectIdentity(BaseModel):
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	issuerAssignedId: Optional[str] = Field(alias="issuerAssignedId", default=None,)
	signInType: Optional[str] = Field(alias="signInType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

