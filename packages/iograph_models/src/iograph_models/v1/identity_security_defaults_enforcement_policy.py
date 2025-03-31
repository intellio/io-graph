from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IdentitySecurityDefaultsEnforcementPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identitySecurityDefaultsEnforcementPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.identitySecurityDefaultsEnforcementPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)

