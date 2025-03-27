from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataReferenceValue(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	value: Optional[IndustryDataReferenceDefinition] = Field(alias="value", default=None,)
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
			if mapping_key == "#microsoft.graph.industryData.fileFormatReferenceValue":
				from .industry_data_file_format_reference_value import IndustryDataFileFormatReferenceValue
				return IndustryDataFileFormatReferenceValue.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.identifierTypeReferenceValue":
				from .industry_data_identifier_type_reference_value import IndustryDataIdentifierTypeReferenceValue
				return IndustryDataIdentifierTypeReferenceValue.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.roleReferenceValue":
				from .industry_data_role_reference_value import IndustryDataRoleReferenceValue
				return IndustryDataRoleReferenceValue.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.sectionRoleReferenceValue":
				from .industry_data_section_role_reference_value import IndustryDataSectionRoleReferenceValue
				return IndustryDataSectionRoleReferenceValue.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.userMatchTargetReferenceValue":
				from .industry_data_user_match_target_reference_value import IndustryDataUserMatchTargetReferenceValue
				return IndustryDataUserMatchTargetReferenceValue.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.yearReferenceValue":
				from .industry_data_year_reference_value import IndustryDataYearReferenceValue
				return IndustryDataYearReferenceValue.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .industry_data_reference_definition import IndustryDataReferenceDefinition

