from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceKey(BaseModel):
	deviceId: Optional[UUID] = Field(alias="deviceId",default=None,)
	keyMaterial: Optional[str] = Field(alias="keyMaterial",default=None,)
	keyType: Optional[str] = Field(alias="keyType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


