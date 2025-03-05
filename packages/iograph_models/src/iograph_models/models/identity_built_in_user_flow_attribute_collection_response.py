from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityBuiltInUserFlowAttributeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[IdentityBuiltInUserFlowAttribute]] = Field(default=None,alias="value",)

from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute

