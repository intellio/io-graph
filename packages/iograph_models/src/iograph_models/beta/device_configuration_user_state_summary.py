from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceConfigurationUserStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceConfigurationUserStateSummary"] = Field(alias="@odata.type",)
	compliantUserCount: Optional[int] = Field(alias="compliantUserCount", default=None,)
	conflictUserCount: Optional[int] = Field(alias="conflictUserCount", default=None,)
	errorUserCount: Optional[int] = Field(alias="errorUserCount", default=None,)
	nonCompliantUserCount: Optional[int] = Field(alias="nonCompliantUserCount", default=None,)
	notApplicableUserCount: Optional[int] = Field(alias="notApplicableUserCount", default=None,)
	remediatedUserCount: Optional[int] = Field(alias="remediatedUserCount", default=None,)
	unknownUserCount: Optional[int] = Field(alias="unknownUserCount", default=None,)

