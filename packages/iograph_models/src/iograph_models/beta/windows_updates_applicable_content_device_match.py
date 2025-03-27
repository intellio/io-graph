from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesApplicableContentDeviceMatch(BaseModel):
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	recommendedBy: Optional[list[str]] = Field(alias="recommendedBy", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


