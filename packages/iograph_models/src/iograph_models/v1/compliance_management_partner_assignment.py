from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class ComplianceManagementPartnerAssignment(BaseModel):
	target: Optional[Union[AllDevicesAssignmentTarget, AllLicensedUsersAssignmentTarget, ConfigurationManagerCollectionAssignmentTarget, ExclusionGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .all_devices_assignment_target import AllDevicesAssignmentTarget
from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget
