from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnsupportedDeviceConfigurationDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UnsupportedDeviceConfigurationDetail]] = Field(alias="value", default=None,)

from .unsupported_device_configuration_detail import UnsupportedDeviceConfigurationDetail
