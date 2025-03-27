from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcUserSettingAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	target: Optional[Union[CloudPcManagementGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

from .cloud_pc_management_group_assignment_target import CloudPcManagementGroupAssignmentTarget

