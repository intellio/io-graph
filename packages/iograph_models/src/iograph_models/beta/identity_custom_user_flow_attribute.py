from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityCustomUserFlowAttribute(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityCustomUserFlowAttribute"] = Field(alias="@odata.type", default="#microsoft.graph.identityCustomUserFlowAttribute")
	dataType: Optional[IdentityUserFlowAttributeDataType | str] = Field(alias="dataType", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	userFlowAttributeType: Optional[IdentityUserFlowAttributeType | str] = Field(alias="userFlowAttributeType", default=None,)

from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType
