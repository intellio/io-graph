from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignPostRequest(BaseModel):
	assignments: Optional[list[CloudPcUserSettingAssignment]] = Field(default=None,alias="assignments",)

from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment

