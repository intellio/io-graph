from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SchedulingGroupInfo(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	schedulingGroupId: Optional[str] = Field(alias="schedulingGroupId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

