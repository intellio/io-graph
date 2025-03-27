from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementCollectionSettingInstance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementCollectionSettingInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementCollectionSettingInstance")
	definitionId: Optional[str] = Field(alias="definitionId", default=None,)
	valueJson: Optional[str] = Field(alias="valueJson", default=None,)
	value: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingInstance, DeviceManagementBooleanSettingInstance, DeviceManagementCollectionSettingInstance, DeviceManagementComplexSettingInstance, DeviceManagementIntegerSettingInstance, DeviceManagementStringSettingInstance]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
from .device_management_string_setting_instance import DeviceManagementStringSettingInstance

