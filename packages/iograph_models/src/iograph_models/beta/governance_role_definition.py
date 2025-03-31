from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GovernanceRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.governanceRoleDefinition"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)
	resource: Optional[GovernanceResource] = Field(alias="resource", default=None,)
	roleSetting: Optional[GovernanceRoleSetting] = Field(alias="roleSetting", default=None,)

from .governance_resource import GovernanceResource
from .governance_role_setting import GovernanceRoleSetting
