from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceManagementConfigurationSimpleSettingValueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceManagementConfigurationIntegerSettingValue, DeviceManagementConfigurationSecretSettingValue, DeviceManagementConfigurationReferenceSettingValue],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
