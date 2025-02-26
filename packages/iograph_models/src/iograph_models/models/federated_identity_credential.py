from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FederatedIdentityCredential(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	audiences: list[str] = Field(alias="audiences",)
	description: Optional[str] = Field(default=None,alias="description",)
	issuer: Optional[str] = Field(default=None,alias="issuer",)
	name: Optional[str] = Field(default=None,alias="name",)
	subject: Optional[str] = Field(default=None,alias="subject",)


