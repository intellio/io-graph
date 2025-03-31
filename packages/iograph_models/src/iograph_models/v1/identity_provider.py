from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityProvider"] = Field(alias="@odata.type",)
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)

