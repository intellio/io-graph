from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidGeneralDeviceConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AndroidGeneralDeviceConfiguration] = Field(alias="value",)

from .android_general_device_configuration import AndroidGeneralDeviceConfiguration

