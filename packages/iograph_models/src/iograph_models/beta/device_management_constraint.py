from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConstraint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.deviceManagementEnumConstraint":
				from .device_management_enum_constraint import DeviceManagementEnumConstraint
				return DeviceManagementEnumConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentSettingSecretConstraint":
				from .device_management_intent_setting_secret_constraint import DeviceManagementIntentSettingSecretConstraint
				return DeviceManagementIntentSettingSecretConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint":
				from .device_management_setting_abstract_implementation_constraint import DeviceManagementSettingAbstractImplementationConstraint
				return DeviceManagementSettingAbstractImplementationConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingAppConstraint":
				from .device_management_setting_app_constraint import DeviceManagementSettingAppConstraint
				return DeviceManagementSettingAppConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingBooleanConstraint":
				from .device_management_setting_boolean_constraint import DeviceManagementSettingBooleanConstraint
				return DeviceManagementSettingBooleanConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingCollectionConstraint":
				from .device_management_setting_collection_constraint import DeviceManagementSettingCollectionConstraint
				return DeviceManagementSettingCollectionConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint":
				from .device_management_setting_enrollment_type_constraint import DeviceManagementSettingEnrollmentTypeConstraint
				return DeviceManagementSettingEnrollmentTypeConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingFileConstraint":
				from .device_management_setting_file_constraint import DeviceManagementSettingFileConstraint
				return DeviceManagementSettingFileConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingIntegerConstraint":
				from .device_management_setting_integer_constraint import DeviceManagementSettingIntegerConstraint
				return DeviceManagementSettingIntegerConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingProfileConstraint":
				from .device_management_setting_profile_constraint import DeviceManagementSettingProfileConstraint
				return DeviceManagementSettingProfileConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingRegexConstraint":
				from .device_management_setting_regex_constraint import DeviceManagementSettingRegexConstraint
				return DeviceManagementSettingRegexConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingRequiredConstraint":
				from .device_management_setting_required_constraint import DeviceManagementSettingRequiredConstraint
				return DeviceManagementSettingRequiredConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingSddlConstraint":
				from .device_management_setting_sddl_constraint import DeviceManagementSettingSddlConstraint
				return DeviceManagementSettingSddlConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingStringLengthConstraint":
				from .device_management_setting_string_length_constraint import DeviceManagementSettingStringLengthConstraint
				return DeviceManagementSettingStringLengthConstraint.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingXmlConstraint":
				from .device_management_setting_xml_constraint import DeviceManagementSettingXmlConstraint
				return DeviceManagementSettingXmlConstraint.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


