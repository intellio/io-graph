from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppleDeviceFeaturesConfigurationBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: SerializeAsAny[Optional[list[AppleDeviceFeaturesConfigurationBase]]] = Field(default=None,alias="value",)

from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

