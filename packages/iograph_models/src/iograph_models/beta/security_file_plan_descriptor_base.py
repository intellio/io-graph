from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFilePlanDescriptorBase(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
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
			if mapping_key == "#microsoft.graph.security.filePlanAppliedCategory":
				from .security_file_plan_applied_category import SecurityFilePlanAppliedCategory
				return SecurityFilePlanAppliedCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanAuthority":
				from .security_file_plan_authority import SecurityFilePlanAuthority
				return SecurityFilePlanAuthority.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanCitation":
				from .security_file_plan_citation import SecurityFilePlanCitation
				return SecurityFilePlanCitation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanDepartment":
				from .security_file_plan_department import SecurityFilePlanDepartment
				return SecurityFilePlanDepartment.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanReference":
				from .security_file_plan_reference import SecurityFilePlanReference
				return SecurityFilePlanReference.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanSubcategory":
				from .security_file_plan_subcategory import SecurityFilePlanSubcategory
				return SecurityFilePlanSubcategory.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


