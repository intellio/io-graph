from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsQualityUpdatePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsQualityUpdatePolicy"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hotpatchEnabled: Optional[bool] = Field(alias="hotpatchEnabled", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	assignments: Optional[list[WindowsQualityUpdatePolicyAssignment]] = Field(alias="assignments", default=None,)

from .windows_quality_update_policy_assignment import WindowsQualityUpdatePolicyAssignment
