from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosNetworkUsageRule(BaseModel):
	cellularDataBlocked: Optional[bool] = Field(alias="cellularDataBlocked", default=None,)
	cellularDataBlockWhenRoaming: Optional[bool] = Field(alias="cellularDataBlockWhenRoaming", default=None,)
	managedApps: Optional[list[AppListItem]] = Field(alias="managedApps", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .app_list_item import AppListItem

