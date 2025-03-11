from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessDevices(BaseModel):
	deviceFilter: Optional[ConditionalAccessFilter] = Field(alias="deviceFilter",default=None,)
	excludeDevices: Optional[list[str]] = Field(alias="excludeDevices",default=None,)
	excludeDeviceStates: Optional[list[str]] = Field(alias="excludeDeviceStates",default=None,)
	includeDevices: Optional[list[str]] = Field(alias="includeDevices",default=None,)
	includeDeviceStates: Optional[list[str]] = Field(alias="includeDeviceStates",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .conditional_access_filter import ConditionalAccessFilter

