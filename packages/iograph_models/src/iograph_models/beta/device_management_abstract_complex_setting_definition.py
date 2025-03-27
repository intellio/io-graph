from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementAbstractComplexSettingDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	constraints: Optional[list[Annotated[Union[DeviceManagementEnumConstraint, DeviceManagementIntentSettingSecretConstraint, DeviceManagementSettingAbstractImplementationConstraint, DeviceManagementSettingAppConstraint, DeviceManagementSettingBooleanConstraint, DeviceManagementSettingCollectionConstraint, DeviceManagementSettingEnrollmentTypeConstraint, DeviceManagementSettingFileConstraint, DeviceManagementSettingIntegerConstraint, DeviceManagementSettingProfileConstraint, DeviceManagementSettingRegexConstraint, DeviceManagementSettingRequiredConstraint, DeviceManagementSettingSddlConstraint, DeviceManagementSettingStringLengthConstraint, DeviceManagementSettingXmlConstraint],Field(discriminator="odata_type")]]] = Field(alias="constraints", default=None,)
	dependencies: Optional[list[DeviceManagementSettingDependency]] = Field(alias="dependencies", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	documentationUrl: Optional[str] = Field(alias="documentationUrl", default=None,)
	headerSubtitle: Optional[str] = Field(alias="headerSubtitle", default=None,)
	headerTitle: Optional[str] = Field(alias="headerTitle", default=None,)
	isTopLevel: Optional[bool] = Field(alias="isTopLevel", default=None,)
	keywords: Optional[list[str]] = Field(alias="keywords", default=None,)
	placeholderText: Optional[str] = Field(alias="placeholderText", default=None,)
	valueType: Optional[DeviceManangementIntentValueType | str] = Field(alias="valueType", default=None,)
	implementations: Optional[list[str]] = Field(alias="implementations", default=None,)

from .device_management_enum_constraint import DeviceManagementEnumConstraint
from .device_management_intent_setting_secret_constraint import DeviceManagementIntentSettingSecretConstraint
from .device_management_setting_abstract_implementation_constraint import DeviceManagementSettingAbstractImplementationConstraint
from .device_management_setting_app_constraint import DeviceManagementSettingAppConstraint
from .device_management_setting_boolean_constraint import DeviceManagementSettingBooleanConstraint
from .device_management_setting_collection_constraint import DeviceManagementSettingCollectionConstraint
from .device_management_setting_enrollment_type_constraint import DeviceManagementSettingEnrollmentTypeConstraint
from .device_management_setting_file_constraint import DeviceManagementSettingFileConstraint
from .device_management_setting_integer_constraint import DeviceManagementSettingIntegerConstraint
from .device_management_setting_profile_constraint import DeviceManagementSettingProfileConstraint
from .device_management_setting_regex_constraint import DeviceManagementSettingRegexConstraint
from .device_management_setting_required_constraint import DeviceManagementSettingRequiredConstraint
from .device_management_setting_sddl_constraint import DeviceManagementSettingSddlConstraint
from .device_management_setting_string_length_constraint import DeviceManagementSettingStringLengthConstraint
from .device_management_setting_xml_constraint import DeviceManagementSettingXmlConstraint
from .device_management_setting_dependency import DeviceManagementSettingDependency
from .device_manangement_intent_value_type import DeviceManangementIntentValueType

