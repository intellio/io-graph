from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Import_office365_device_configuration_policiesPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementIntent]] = Field(alias="value", default=None,)

from .device_management_intent import DeviceManagementIntent
