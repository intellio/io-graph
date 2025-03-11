from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyUploadedPresentation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition",default=None,)

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
			if mapping_key == "#microsoft.graph.groupPolicyPresentationCheckBox":
				from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
				return GroupPolicyPresentationCheckBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationComboBox":
				from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
				return GroupPolicyPresentationComboBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationDecimalTextBox":
				from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
				return GroupPolicyPresentationDecimalTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationDropdownList":
				from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
				return GroupPolicyPresentationDropdownList.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationListBox":
				from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
				return GroupPolicyPresentationListBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox":
				from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
				return GroupPolicyPresentationLongDecimalTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationMultiTextBox":
				from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
				return GroupPolicyPresentationMultiTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationText":
				from .group_policy_presentation_text import GroupPolicyPresentationText
				return GroupPolicyPresentationText.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationTextBox":
				from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
				return GroupPolicyPresentationTextBox.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .group_policy_definition import GroupPolicyDefinition

