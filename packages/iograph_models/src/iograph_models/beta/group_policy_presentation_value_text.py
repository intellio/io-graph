from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationValueText(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definitionValue: Optional[GroupPolicyDefinitionValue] = Field(alias="definitionValue", default=None,)
	presentation: Optional[Union[GroupPolicyUploadedPresentation, GroupPolicyPresentationCheckBox, GroupPolicyPresentationComboBox, GroupPolicyPresentationDecimalTextBox, GroupPolicyPresentationDropdownList, GroupPolicyPresentationListBox, GroupPolicyPresentationLongDecimalTextBox, GroupPolicyPresentationMultiTextBox, GroupPolicyPresentationText, GroupPolicyPresentationTextBox]] = Field(alias="presentation", default=None,discriminator="odata_type", )
	value: Optional[str] = Field(alias="value", default=None,)

from .group_policy_definition_value import GroupPolicyDefinitionValue
from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation
from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
from .group_policy_presentation_text import GroupPolicyPresentationText
from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

