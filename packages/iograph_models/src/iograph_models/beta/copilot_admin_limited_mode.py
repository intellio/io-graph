from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CopilotAdminLimitedMode(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	isEnabledForGroup: Optional[bool] = Field(alias="isEnabledForGroup", default=None,)


