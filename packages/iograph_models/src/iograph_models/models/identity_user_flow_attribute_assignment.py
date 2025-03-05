from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityUserFlowAttributeAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isOptional: Optional[bool] = Field(default=None,alias="isOptional",)
	requiresVerification: Optional[bool] = Field(default=None,alias="requiresVerification",)
	userAttributeValues: Optional[list[UserAttributeValuesItem]] = Field(default=None,alias="userAttributeValues",)
	userInputType: Optional[IdentityUserFlowAttributeInputType] = Field(default=None,alias="userInputType",)
	userAttribute: Optional[IdentityUserFlowAttribute] = Field(default=None,alias="userAttribute",)

from .user_attribute_values_item import UserAttributeValuesItem
from .identity_user_flow_attribute_input_type import IdentityUserFlowAttributeInputType
from .identity_user_flow_attribute import IdentityUserFlowAttribute

