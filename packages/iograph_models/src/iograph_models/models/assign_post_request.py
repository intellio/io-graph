from __future__ import annotations
from pydantic import BaseModel, Field


class AssignPostRequest(BaseModel):
	assignments: list[CloudPcUserSettingAssignment] = Field(alias="assignments",)

from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment

