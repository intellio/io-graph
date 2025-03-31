from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceProperties(BaseModel):
	deviceIdentifiers: Optional[list[str]] = Field(alias="deviceIdentifiers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

