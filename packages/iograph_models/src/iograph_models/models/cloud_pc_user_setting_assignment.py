from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcUserSettingAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	target: SerializeAsAny[Optional[CloudPcManagementAssignmentTarget]] = Field(alias="target",default=None,)

from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

