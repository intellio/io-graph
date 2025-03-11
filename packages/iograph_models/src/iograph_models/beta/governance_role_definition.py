from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernanceRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	templateId: Optional[str] = Field(alias="templateId",default=None,)
	resource: Optional[GovernanceResource] = Field(alias="resource",default=None,)
	roleSetting: Optional[GovernanceRoleSetting] = Field(alias="roleSetting",default=None,)

from .governance_resource import GovernanceResource
from .governance_role_setting import GovernanceRoleSetting

