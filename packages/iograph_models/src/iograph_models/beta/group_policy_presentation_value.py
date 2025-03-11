from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationValue(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definitionValue: Optional[GroupPolicyDefinitionValue] = Field(alias="definitionValue",default=None,)
	presentation: SerializeAsAny[Optional[GroupPolicyPresentation]] = Field(alias="presentation",default=None,)

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
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueBoolean":
				from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
				return GroupPolicyPresentationValueBoolean.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueDecimal":
				from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
				return GroupPolicyPresentationValueDecimal.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueList":
				from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
				return GroupPolicyPresentationValueList.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueLongDecimal":
				from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
				return GroupPolicyPresentationValueLongDecimal.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueMultiText":
				from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
				return GroupPolicyPresentationValueMultiText.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueText":
				from .group_policy_presentation_value_text import GroupPolicyPresentationValueText
				return GroupPolicyPresentationValueText.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .group_policy_definition_value import GroupPolicyDefinitionValue
from .group_policy_presentation import GroupPolicyPresentation

