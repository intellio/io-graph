from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosNetworkUsageRule(BaseModel):
	cellularDataBlocked: Optional[bool] = Field(default=None,alias="cellularDataBlocked",)
	cellularDataBlockWhenRoaming: Optional[bool] = Field(default=None,alias="cellularDataBlockWhenRoaming",)
	managedApps: Optional[list[AppListItem]] = Field(default=None,alias="managedApps",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .app_list_item import AppListItem

