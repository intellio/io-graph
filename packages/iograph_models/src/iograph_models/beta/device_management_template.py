from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	intentCount: Optional[int] = Field(alias="intentCount", default=None,)
	isDeprecated: Optional[bool] = Field(alias="isDeprecated", default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	templateSubtype: Optional[DeviceManagementTemplateSubtype | str] = Field(alias="templateSubtype", default=None,)
	templateType: Optional[DeviceManagementTemplateType | str] = Field(alias="templateType", default=None,)
	versionInfo: Optional[str] = Field(alias="versionInfo", default=None,)
	categories: Optional[list[DeviceManagementTemplateSettingCategory]] = Field(alias="categories", default=None,)
	migratableTo: Optional[list[Annotated[Union[SecurityBaselineTemplate],Field(discriminator="odata_type")]]] = Field(alias="migratableTo", default=None,)
	settings: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingInstance, DeviceManagementBooleanSettingInstance, DeviceManagementCollectionSettingInstance, DeviceManagementComplexSettingInstance, DeviceManagementIntegerSettingInstance, DeviceManagementStringSettingInstance],Field(discriminator="odata_type")]]] = Field(alias="settings", default=None,)

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
			if mapping_key == "#microsoft.graph.securityBaselineTemplate":
				from .security_baseline_template import SecurityBaselineTemplate
				return SecurityBaselineTemplate.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .policy_platform_type import PolicyPlatformType
from .device_management_template_subtype import DeviceManagementTemplateSubtype
from .device_management_template_type import DeviceManagementTemplateType
from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
from .security_baseline_template import SecurityBaselineTemplate
from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
from .device_management_string_setting_instance import DeviceManagementStringSettingInstance

