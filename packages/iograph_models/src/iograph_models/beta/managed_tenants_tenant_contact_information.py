from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsTenantContactInformation(BaseModel):
	email: Optional[str] = Field(alias="email", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	phone: Optional[str] = Field(alias="phone", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

