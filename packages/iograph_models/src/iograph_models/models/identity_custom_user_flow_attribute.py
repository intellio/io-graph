from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityCustomUserFlowAttribute(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	dataType: Optional[str | IdentityUserFlowAttributeDataType] = Field(alias="dataType",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	userFlowAttributeType: Optional[str | IdentityUserFlowAttributeType] = Field(alias="userFlowAttributeType",default=None,)

from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType

