from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class GroupPolicyPresentationValue(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definitionValue: Optional[GroupPolicyDefinitionValue] = Field(alias="definitionValue", default=None,)
	presentation: Optional[Union[GroupPolicyPresentationCheckBox, GroupPolicyPresentationComboBox, GroupPolicyPresentationDecimalTextBox, GroupPolicyPresentationDropdownList, GroupPolicyPresentationListBox, GroupPolicyPresentationLongDecimalTextBox, GroupPolicyPresentationMultiTextBox, GroupPolicyPresentationText, GroupPolicyPresentationTextBox]] = Field(alias="presentation", default=None,discriminator="odata_type", )

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
from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
from .group_policy_presentation_text import GroupPolicyPresentationText
from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
