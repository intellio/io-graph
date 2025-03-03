from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcUserSetting(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	localAdminEnabled: Optional[bool] = Field(default=None,alias="localAdminEnabled",)
	resetEnabled: Optional[bool] = Field(default=None,alias="resetEnabled",)
	restorePointSetting: Optional[CloudPcRestorePointSetting] = Field(default=None,alias="restorePointSetting",)
	assignments: Optional[list[CloudPcUserSettingAssignment]] = Field(default=None,alias="assignments",)

from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment

