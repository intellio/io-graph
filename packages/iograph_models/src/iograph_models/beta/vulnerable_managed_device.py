from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VulnerableManagedDevice(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId",default=None,)


