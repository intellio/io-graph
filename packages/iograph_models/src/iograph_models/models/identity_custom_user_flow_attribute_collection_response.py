from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityCustomUserFlowAttributeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IdentityCustomUserFlowAttribute] = Field(alias="value",)

from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

