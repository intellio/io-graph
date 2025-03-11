from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementAbstractComplexSettingDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceManagementAbstractComplexSettingDefinition]] = Field(alias="value",default=None,)

from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition

