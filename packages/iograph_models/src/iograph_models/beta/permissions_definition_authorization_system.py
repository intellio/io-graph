from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PermissionsDefinitionAuthorizationSystem(BaseModel):
	authorizationSystemId: Optional[str] = Field(alias="authorizationSystemId", default=None,)
	authorizationSystemType: Optional[str] = Field(alias="authorizationSystemType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

