from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PolicySetAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.policySetAssignment"] = Field(alias="@odata.type",)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	target: Optional[Union[AllDevicesAssignmentTarget, AllLicensedUsersAssignmentTarget, AndroidFotaDeploymentAssignmentTarget, ConfigurationManagerCollectionAssignmentTarget, ExclusionGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

from .all_devices_assignment_target import AllDevicesAssignmentTarget
from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget
