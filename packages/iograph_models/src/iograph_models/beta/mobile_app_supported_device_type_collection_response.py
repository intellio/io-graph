from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppSupportedDeviceTypeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MobileAppSupportedDeviceType]] = Field(alias="value",default=None,)

from .mobile_app_supported_device_type import MobileAppSupportedDeviceType

