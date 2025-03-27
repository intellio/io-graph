from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBaselineStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	conflictCount: Optional[int] = Field(alias="conflictCount", default=None,)
	errorCount: Optional[int] = Field(alias="errorCount", default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount", default=None,)
	notSecureCount: Optional[int] = Field(alias="notSecureCount", default=None,)
	secureCount: Optional[int] = Field(alias="secureCount", default=None,)
	unknownCount: Optional[int] = Field(alias="unknownCount", default=None,)

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
			if mapping_key == "#microsoft.graph.securityBaselineCategoryStateSummary":
				from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
				return SecurityBaselineCategoryStateSummary.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


