from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosGeneralDeviceConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosGeneralDeviceConfiguration] = Field(alias="value",)

from .ios_general_device_configuration import IosGeneralDeviceConfiguration

