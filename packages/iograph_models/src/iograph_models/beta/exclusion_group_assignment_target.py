from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExclusionGroupAssignmentTarget(BaseModel):
	deviceAndAppManagementAssignmentFilterId: Optional[str] = Field(alias="deviceAndAppManagementAssignmentFilterId", default=None,)
	deviceAndAppManagementAssignmentFilterType: Optional[DeviceAndAppManagementAssignmentFilterType | str] = Field(alias="deviceAndAppManagementAssignmentFilterType", default=None,)
	odata_type: Literal["#microsoft.graph.exclusionGroupAssignmentTarget"] = Field(alias="@odata.type", default="#microsoft.graph.exclusionGroupAssignmentTarget")
	groupId: Optional[str] = Field(alias="groupId", default=None,)

from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

