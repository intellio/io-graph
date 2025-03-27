from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Create_instancePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	settingsDelta: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingInstance, DeviceManagementBooleanSettingInstance, DeviceManagementCollectionSettingInstance, DeviceManagementComplexSettingInstance, DeviceManagementIntegerSettingInstance, DeviceManagementStringSettingInstance]],Field(discriminator="odata_type")]]] = Field(alias="settingsDelta", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)

from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
from .device_management_string_setting_instance import DeviceManagementStringSettingInstance

