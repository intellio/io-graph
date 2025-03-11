from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcUserSetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	localAdminEnabled: Optional[bool] = Field(alias="localAdminEnabled",default=None,)
	resetEnabled: Optional[bool] = Field(alias="resetEnabled",default=None,)
	restorePointSetting: Optional[CloudPcRestorePointSetting] = Field(alias="restorePointSetting",default=None,)
	assignments: Optional[list[CloudPcUserSettingAssignment]] = Field(alias="assignments",default=None,)

from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment

