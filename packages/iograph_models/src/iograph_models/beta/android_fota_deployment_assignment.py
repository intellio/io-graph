from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AndroidFotaDeploymentAssignment(BaseModel):
	assignmentTarget: Optional[Union[AllDevicesAssignmentTarget, AllLicensedUsersAssignmentTarget, AndroidFotaDeploymentAssignmentTarget, ConfigurationManagerCollectionAssignmentTarget, ExclusionGroupAssignmentTarget]] = Field(alias="assignmentTarget", default=None,discriminator="odata_type", )
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	target: Optional[AndroidFotaDeploymentAssignmentTarget] = Field(alias="target", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .all_devices_assignment_target import AllDevicesAssignmentTarget
from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget
