from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementComplexSettingDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	constraints: SerializeAsAny[Optional[list[DeviceManagementConstraint]]] = Field(alias="constraints",default=None,)
	dependencies: Optional[list[DeviceManagementSettingDependency]] = Field(alias="dependencies",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	documentationUrl: Optional[str] = Field(alias="documentationUrl",default=None,)
	headerSubtitle: Optional[str] = Field(alias="headerSubtitle",default=None,)
	headerTitle: Optional[str] = Field(alias="headerTitle",default=None,)
	isTopLevel: Optional[bool] = Field(alias="isTopLevel",default=None,)
	keywords: Optional[list[str]] = Field(alias="keywords",default=None,)
	placeholderText: Optional[str] = Field(alias="placeholderText",default=None,)
	valueType: Optional[DeviceManangementIntentValueType | str] = Field(alias="valueType",default=None,)
	propertyDefinitionIds: Optional[list[str]] = Field(alias="propertyDefinitionIds",default=None,)

from .device_management_constraint import DeviceManagementConstraint
from .device_management_setting_dependency import DeviceManagementSettingDependency
from .device_manangement_intent_value_type import DeviceManangementIntentValueType

