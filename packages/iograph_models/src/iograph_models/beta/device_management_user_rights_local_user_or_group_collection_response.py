from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementUserRightsLocalUserOrGroupCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementUserRightsLocalUserOrGroup]] = Field(alias="value", default=None,)

from .device_management_user_rights_local_user_or_group import DeviceManagementUserRightsLocalUserOrGroup

