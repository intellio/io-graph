from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSDeviceFeaturesConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MacOSDeviceFeaturesConfiguration]] = Field(default=None,alias="value",)

from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

