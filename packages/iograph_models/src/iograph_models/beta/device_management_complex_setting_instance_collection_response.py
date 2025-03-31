from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementComplexSettingInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementComplexSettingInstance]] = Field(alias="value", default=None,)

from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
