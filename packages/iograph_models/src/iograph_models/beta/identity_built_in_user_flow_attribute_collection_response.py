from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityBuiltInUserFlowAttributeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityBuiltInUserFlowAttribute]] = Field(alias="value", default=None,)

from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute

