from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimTransformation(BaseModel):
	input: Optional[TransformationAttribute] = Field(alias="input", default=None,)
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
			if mapping_key == "#microsoft.graph.containsTransformation":
				from .contains_transformation import ContainsTransformation
				return ContainsTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.endsWithTransformation":
				from .ends_with_transformation import EndsWithTransformation
				return EndsWithTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.extractAlphaTransformation":
				from .extract_alpha_transformation import ExtractAlphaTransformation
				return ExtractAlphaTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.extractMailPrefixTransformation":
				from .extract_mail_prefix_transformation import ExtractMailPrefixTransformation
				return ExtractMailPrefixTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.extractNumberTransformation":
				from .extract_number_transformation import ExtractNumberTransformation
				return ExtractNumberTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.extractTransformation":
				from .extract_transformation import ExtractTransformation
				return ExtractTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.ifEmptyTransformation":
				from .if_empty_transformation import IfEmptyTransformation
				return IfEmptyTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.ifNotEmptyTransformation":
				from .if_not_empty_transformation import IfNotEmptyTransformation
				return IfNotEmptyTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.joinTransformation":
				from .join_transformation import JoinTransformation
				return JoinTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.regexReplaceTransformation":
				from .regex_replace_transformation import RegexReplaceTransformation
				return RegexReplaceTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.startsWithTransformation":
				from .starts_with_transformation import StartsWithTransformation
				return StartsWithTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.substringTransformation":
				from .substring_transformation import SubstringTransformation
				return SubstringTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.toLowercaseTransformation":
				from .to_lowercase_transformation import ToLowercaseTransformation
				return ToLowercaseTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.toUppercaseTransformation":
				from .to_uppercase_transformation import ToUppercaseTransformation
				return ToUppercaseTransformation.model_validate(data)
			if mapping_key == "#microsoft.graph.trimTransformation":
				from .trim_transformation import TrimTransformation
				return TrimTransformation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .transformation_attribute import TransformationAttribute

