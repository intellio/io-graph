from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.userIdentity")
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

