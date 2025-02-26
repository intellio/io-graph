from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementPartnerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DeviceManagementPartner] = Field(alias="value",)

from .device_management_partner import DeviceManagementPartner

