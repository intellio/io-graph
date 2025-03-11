from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidFotaDeploymentAssignment(BaseModel):
	assignmentTarget: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="assignmentTarget",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	target: Optional[AndroidFotaDeploymentAssignmentTarget] = Field(alias="target",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget

