from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityCustomUserFlowAttributeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityCustomUserFlowAttribute]] = Field(alias="value", default=None,)

from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

