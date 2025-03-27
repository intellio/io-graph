from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	categoryPath: Optional[str] = Field(alias="categoryPath", default=None,)
	classType: Optional[GroupPolicyDefinitionClassType | str] = Field(alias="classType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	explainText: Optional[str] = Field(alias="explainText", default=None,)
	groupPolicyCategoryId: Optional[UUID] = Field(alias="groupPolicyCategoryId", default=None,)
	hasRelatedDefinitions: Optional[bool] = Field(alias="hasRelatedDefinitions", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	minDeviceCspVersion: Optional[str] = Field(alias="minDeviceCspVersion", default=None,)
	minUserCspVersion: Optional[str] = Field(alias="minUserCspVersion", default=None,)
	policyType: Optional[GroupPolicyType | str] = Field(alias="policyType", default=None,)
	supportedOn: Optional[str] = Field(alias="supportedOn", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	category: Optional[GroupPolicyCategory] = Field(alias="category", default=None,)
	definitionFile: Optional[Union[GroupPolicyUploadedDefinitionFile]] = Field(alias="definitionFile", default=None,discriminator="odata_type", )
	nextVersionDefinition: Optional[GroupPolicyDefinition] = Field(alias="nextVersionDefinition", default=None,)
	presentations: Optional[list[Annotated[Union[GroupPolicyUploadedPresentation, GroupPolicyPresentationCheckBox, GroupPolicyPresentationComboBox, GroupPolicyPresentationDecimalTextBox, GroupPolicyPresentationDropdownList, GroupPolicyPresentationListBox, GroupPolicyPresentationLongDecimalTextBox, GroupPolicyPresentationMultiTextBox, GroupPolicyPresentationText, GroupPolicyPresentationTextBox]],Field(discriminator="odata_type")]]] = Field(alias="presentations", default=None,)
	previousVersionDefinition: Optional[GroupPolicyDefinition] = Field(alias="previousVersionDefinition", default=None,)

from .group_policy_definition_class_type import GroupPolicyDefinitionClassType
from .group_policy_type import GroupPolicyType
from .group_policy_category import GroupPolicyCategory
from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
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

