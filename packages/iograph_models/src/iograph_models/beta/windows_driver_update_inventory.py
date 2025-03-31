from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsDriverUpdateInventory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsDriverUpdateInventory"] = Field(alias="@odata.type",)
	applicableDeviceCount: Optional[int] = Field(alias="applicableDeviceCount", default=None,)
	approvalStatus: Optional[DriverApprovalStatus | str] = Field(alias="approvalStatus", default=None,)
	category: Optional[DriverCategory | str] = Field(alias="category", default=None,)
	deployDateTime: Optional[datetime] = Field(alias="deployDateTime", default=None,)
	driverClass: Optional[str] = Field(alias="driverClass", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

from .driver_approval_status import DriverApprovalStatus
from .driver_category import DriverCategory
