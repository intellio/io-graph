from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSGeneralDeviceConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MacOSGeneralDeviceConfiguration] = Field(alias="value",)

from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration

