from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class WindowsDriverUpdateProfileAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsDriverUpdateProfileAssignment"] = Field(alias="@odata.type",)
	target: Optional[Union[AllDevicesAssignmentTarget, AllLicensedUsersAssignmentTarget, AndroidFotaDeploymentAssignmentTarget, ConfigurationManagerCollectionAssignmentTarget, ExclusionGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

from .all_devices_assignment_target import AllDevicesAssignmentTarget
from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget
