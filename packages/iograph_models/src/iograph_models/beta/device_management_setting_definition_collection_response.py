from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingDefinition, DeviceManagementCollectionSettingDefinition, DeviceManagementComplexSettingDefinition],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition

