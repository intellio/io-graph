from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BitlockerRecoveryKey(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	key: Optional[str] = Field(default=None,alias="key",)
	volumeType: Optional[VolumeType] = Field(default=None,alias="volumeType",)

from .volume_type import VolumeType

