from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataRoleGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	roles: Optional[list[IndustryDataRoleReferenceValue]] = Field(alias="roles", default=None,)

from .industry_data_role_reference_value import IndustryDataRoleReferenceValue

