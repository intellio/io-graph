from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityUserFlowAttributeAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityUserFlowAttributeAssignment]] = Field(alias="value", default=None,)

from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
