from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementCollectionSettingInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceManagementCollectionSettingInstance]] = Field(alias="value",default=None,)

from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance

