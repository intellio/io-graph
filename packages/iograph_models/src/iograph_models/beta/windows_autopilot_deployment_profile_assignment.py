from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class WindowsAutopilotDeploymentProfileAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsAutopilotDeploymentProfileAssignment"] = Field(alias="@odata.type",)
	source: Optional[DeviceAndAppManagementAssignmentSource | str] = Field(alias="source", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	target: Optional[Union[AllDevicesAssignmentTarget, AllLicensedUsersAssignmentTarget, AndroidFotaDeploymentAssignmentTarget, ConfigurationManagerCollectionAssignmentTarget, ExclusionGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource
from .all_devices_assignment_target import AllDevicesAssignmentTarget
from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget
