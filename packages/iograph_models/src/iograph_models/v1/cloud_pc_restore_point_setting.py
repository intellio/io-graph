from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcRestorePointSetting(BaseModel):
	frequencyType: Optional[CloudPcRestorePointFrequencyType | str] = Field(alias="frequencyType", default=None,)
	userRestoreEnabled: Optional[bool] = Field(alias="userRestoreEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_restore_point_frequency_type import CloudPcRestorePointFrequencyType
