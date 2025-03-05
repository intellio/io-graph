from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityProvider(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientId: Optional[str] = Field(default=None,alias="clientId",)
	clientSecret: Optional[str] = Field(default=None,alias="clientSecret",)
	name: Optional[str] = Field(default=None,alias="name",)
	type: Optional[str] = Field(default=None,alias="type",)


