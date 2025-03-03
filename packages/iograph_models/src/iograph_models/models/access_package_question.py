from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class AccessPackageQuestion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isAnswerEditable: Optional[bool] = Field(default=None,alias="isAnswerEditable",)
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(default=None,alias="localizations",)
	sequence: Optional[int] = Field(default=None,alias="sequence",)
	text: Optional[str] = Field(default=None,alias="text",)

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
			if mapping_key == "#microsoft.graph.accessPackageMultipleChoiceQuestion":
				from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
				return AccessPackageMultipleChoiceQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageTextInputQuestion":
				from .access_package_text_input_question import AccessPackageTextInputQuestion
				return AccessPackageTextInputQuestion.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .access_package_localized_text import AccessPackageLocalizedText

