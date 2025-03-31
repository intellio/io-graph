from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobilityManagementPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MobilityManagementPolicy]] = Field(alias="value", default=None,)

from .mobility_management_policy import MobilityManagementPolicy
