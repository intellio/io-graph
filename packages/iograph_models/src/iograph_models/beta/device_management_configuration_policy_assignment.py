from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationPolicyAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	source: Optional[DeviceAndAppManagementAssignmentSource | str] = Field(alias="source",default=None,)
	sourceId: Optional[str] = Field(alias="sourceId",default=None,)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="target",default=None,)

from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

