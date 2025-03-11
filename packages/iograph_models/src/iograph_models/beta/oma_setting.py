from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class OmaSetting(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isEncrypted: Optional[bool] = Field(alias="isEncrypted",default=None,)
	omaUri: Optional[str] = Field(alias="omaUri",default=None,)
	secretReferenceValueId: Optional[str] = Field(alias="secretReferenceValueId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.omaSettingBase64":
				from .oma_setting_base64 import OmaSettingBase64
				return OmaSettingBase64.model_validate(data)
			if mapping_key == "#microsoft.graph.omaSettingBoolean":
				from .oma_setting_boolean import OmaSettingBoolean
				return OmaSettingBoolean.model_validate(data)
			if mapping_key == "#microsoft.graph.omaSettingDateTime":
				from .oma_setting_date_time import OmaSettingDateTime
				return OmaSettingDateTime.model_validate(data)
			if mapping_key == "#microsoft.graph.omaSettingFloatingPoint":
				from .oma_setting_floating_point import OmaSettingFloatingPoint
				return OmaSettingFloatingPoint.model_validate(data)
			if mapping_key == "#microsoft.graph.omaSettingInteger":
				from .oma_setting_integer import OmaSettingInteger
				return OmaSettingInteger.model_validate(data)
			if mapping_key == "#microsoft.graph.omaSettingString":
				from .oma_setting_string import OmaSettingString
				return OmaSettingString.model_validate(data)
			if mapping_key == "#microsoft.graph.omaSettingStringXml":
				from .oma_setting_string_xml import OmaSettingStringXml
				return OmaSettingStringXml.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


