from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernancePermission(BaseModel):
	accessLevel: Optional[str] = Field(alias="accessLevel", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	isEligible: Optional[bool] = Field(alias="isEligible", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


