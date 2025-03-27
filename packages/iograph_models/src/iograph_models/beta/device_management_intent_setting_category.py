from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentSettingCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hasRequiredSetting: Optional[bool] = Field(alias="hasRequiredSetting", default=None,)
	settingDefinitions: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingDefinition, DeviceManagementCollectionSettingDefinition, DeviceManagementComplexSettingDefinition],Field(discriminator="odata_type")]]] = Field(alias="settingDefinitions", default=None,)
	settings: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingInstance, DeviceManagementBooleanSettingInstance, DeviceManagementCollectionSettingInstance, DeviceManagementComplexSettingInstance, DeviceManagementIntegerSettingInstance, DeviceManagementStringSettingInstance],Field(discriminator="odata_type")]]] = Field(alias="settings", default=None,)

from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
from .device_management_string_setting_instance import DeviceManagementStringSettingInstance

