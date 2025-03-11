from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BitlockerRecoveryKey(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	key: Optional[str] = Field(alias="key",default=None,)
	volumeType: Optional[VolumeType | str] = Field(alias="volumeType",default=None,)

from .volume_type import VolumeType

