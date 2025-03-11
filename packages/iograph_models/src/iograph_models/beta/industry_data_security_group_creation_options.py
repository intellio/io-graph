from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataSecurityGroupCreationOptions(BaseModel):
	createBasedOnOrgPlusRoleGroup: Optional[bool] = Field(alias="createBasedOnOrgPlusRoleGroup",default=None,)
	createBasedOnRoleGroup: Optional[bool] = Field(alias="createBasedOnRoleGroup",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


