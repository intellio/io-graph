from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealth(BaseModel):
	lastConnectionTime: Optional[datetime] = Field(alias="lastConnectionTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


