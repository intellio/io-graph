from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcUserSettingAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	target: SerializeAsAny[Optional[CloudPcManagementAssignmentTarget]] = Field(default=None,alias="target",)

from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

