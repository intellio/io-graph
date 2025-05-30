from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AppleDeviceFeaturesConfigurationBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IosDeviceFeaturesConfiguration, MacOSDeviceFeaturesConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
