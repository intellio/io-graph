from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcRestorePointSetting(BaseModel):
	frequencyType: Optional[CloudPcRestorePointFrequencyType] = Field(default=None,alias="frequencyType",)
	userRestoreEnabled: Optional[bool] = Field(default=None,alias="userRestoreEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cloud_pc_restore_point_frequency_type import CloudPcRestorePointFrequencyType

