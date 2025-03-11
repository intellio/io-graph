from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Bulk_restore_cloud_pcPostRequest(BaseModel):
	managedDeviceIds: Optional[list[str]] = Field(alias="managedDeviceIds",default=None,)
	restorePointDateTime: Optional[datetime] = Field(alias="restorePointDateTime",default=None,)
	timeRange: Optional[RestoreTimeRange | str] = Field(alias="timeRange",default=None,)

from .restore_time_range import RestoreTimeRange

