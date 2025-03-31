from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcUserSettingAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcUserSettingAssignment"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	target: Optional[Union[CloudPcManagementGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

from .cloud_pc_management_group_assignment_target import CloudPcManagementGroupAssignmentTarget
