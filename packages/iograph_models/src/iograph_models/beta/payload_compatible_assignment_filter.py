from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PayloadCompatibleAssignmentFilter(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.payloadCompatibleAssignmentFilter"] = Field(alias="@odata.type", default="#microsoft.graph.payloadCompatibleAssignmentFilter")
	assignmentFilterManagementType: Optional[AssignmentFilterManagementType | str] = Field(alias="assignmentFilterManagementType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	payloads: Optional[list[PayloadByFilter]] = Field(alias="payloads", default=None,)
	platform: Optional[DevicePlatformType | str] = Field(alias="platform", default=None,)
	roleScopeTags: Optional[list[str]] = Field(alias="roleScopeTags", default=None,)
	rule: Optional[str] = Field(alias="rule", default=None,)
	payloadType: Optional[AssignmentFilterPayloadType | str] = Field(alias="payloadType", default=None,)

from .assignment_filter_management_type import AssignmentFilterManagementType
from .payload_by_filter import PayloadByFilter
from .device_platform_type import DevicePlatformType
from .assignment_filter_payload_type import AssignmentFilterPayloadType
