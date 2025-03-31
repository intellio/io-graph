from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AccessPackageQuestion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isAnswerEditable: Optional[bool] = Field(alias="isAnswerEditable", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(alias="localizations", default=None,)
	sequence: Optional[int] = Field(alias="sequence", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)

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
