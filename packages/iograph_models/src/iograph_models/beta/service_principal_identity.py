from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServicePrincipalIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.servicePrincipalIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.servicePrincipalIdentity")
	appId: Optional[str] = Field(alias="appId", default=None,)

