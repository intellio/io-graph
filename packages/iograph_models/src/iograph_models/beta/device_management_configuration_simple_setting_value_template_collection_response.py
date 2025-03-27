from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSimpleSettingValueTemplateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceManagementConfigurationIntegerSettingValueTemplate, DeviceManagementConfigurationStringSettingValueTemplate],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_management_configuration_integer_setting_value_template import DeviceManagementConfigurationIntegerSettingValueTemplate
from .device_management_configuration_string_setting_value_template import DeviceManagementConfigurationStringSettingValueTemplate

