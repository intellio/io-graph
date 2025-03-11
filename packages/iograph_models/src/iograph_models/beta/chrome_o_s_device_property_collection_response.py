from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChromeOSDevicePropertyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ChromeOSDeviceProperty]] = Field(alias="value",default=None,)

from .chrome_o_s_device_property import ChromeOSDeviceProperty

