from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	runRemediationScript: Optional[bool] = Field(alias="runRemediationScript",default=None,)
	runSchedule: SerializeAsAny[Optional[DeviceHealthScriptRunSchedule]] = Field(alias="runSchedule",default=None,)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="target",default=None,)

from .device_health_script_run_schedule import DeviceHealthScriptRunSchedule
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

