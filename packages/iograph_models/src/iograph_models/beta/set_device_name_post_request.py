from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_device_namePostRequest(BaseModel):
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)


