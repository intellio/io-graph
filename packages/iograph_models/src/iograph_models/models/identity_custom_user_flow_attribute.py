from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityCustomUserFlowAttribute(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	dataType: Optional[IdentityUserFlowAttributeDataType] = Field(default=None,alias="dataType",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	userFlowAttributeType: Optional[IdentityUserFlowAttributeType] = Field(default=None,alias="userFlowAttributeType",)

from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType

