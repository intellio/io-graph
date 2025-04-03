from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IndustryDataRoleGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.roleGroup"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.roleGroup")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	roles: Optional[list[IndustryDataRoleReferenceValue]] = Field(alias="roles", default=None,)

from .industry_data_role_reference_value import IndustryDataRoleReferenceValue
