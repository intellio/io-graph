from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyUploadedPresentationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[GroupPolicyPresentationCheckBox, GroupPolicyPresentationComboBox, GroupPolicyPresentationDecimalTextBox, GroupPolicyPresentationDropdownList, GroupPolicyPresentationListBox, GroupPolicyPresentationLongDecimalTextBox, GroupPolicyPresentationMultiTextBox, GroupPolicyPresentationText, GroupPolicyPresentationTextBox],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
from .group_policy_presentation_text import GroupPolicyPresentationText
from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

