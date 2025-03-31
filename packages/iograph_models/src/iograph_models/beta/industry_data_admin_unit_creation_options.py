from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataAdminUnitCreationOptions(BaseModel):
	createBasedOnOrg: Optional[bool] = Field(alias="createBasedOnOrg", default=None,)
	createBasedOnOrgPlusRoleGroup: Optional[bool] = Field(alias="createBasedOnOrgPlusRoleGroup", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

