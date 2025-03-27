from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityUserFlowAttributeAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isOptional: Optional[bool] = Field(alias="isOptional", default=None,)
	requiresVerification: Optional[bool] = Field(alias="requiresVerification", default=None,)
	userAttributeValues: Optional[list[UserAttributeValuesItem]] = Field(alias="userAttributeValues", default=None,)
	userInputType: Optional[IdentityUserFlowAttributeInputType | str] = Field(alias="userInputType", default=None,)
	userAttribute: Optional[Union[IdentityBuiltInUserFlowAttribute, IdentityCustomUserFlowAttribute]] = Field(alias="userAttribute", default=None,discriminator="odata_type", )

from .user_attribute_values_item import UserAttributeValuesItem
from .identity_user_flow_attribute_input_type import IdentityUserFlowAttributeInputType
from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

