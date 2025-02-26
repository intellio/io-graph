from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectIdentity(BaseModel):
	issuer: Optional[str] = Field(default=None,alias="issuer",)
	issuerAssignedId: Optional[str] = Field(default=None,alias="issuerAssignedId",)
	signInType: Optional[str] = Field(default=None,alias="signInType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


