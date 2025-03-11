from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GovernanceRoleSetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	adminEligibleSettings: Optional[list[GovernanceRuleSetting]] = Field(alias="adminEligibleSettings",default=None,)
	adminMemberSettings: Optional[list[GovernanceRuleSetting]] = Field(alias="adminMemberSettings",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	lastUpdatedBy: Optional[str] = Field(alias="lastUpdatedBy",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	userEligibleSettings: Optional[list[GovernanceRuleSetting]] = Field(alias="userEligibleSettings",default=None,)
	userMemberSettings: Optional[list[GovernanceRuleSetting]] = Field(alias="userMemberSettings",default=None,)
	resource: Optional[GovernanceResource] = Field(alias="resource",default=None,)
	roleDefinition: Optional[GovernanceRoleDefinition] = Field(alias="roleDefinition",default=None,)

from .governance_rule_setting import GovernanceRuleSetting
from .governance_rule_setting import GovernanceRuleSetting
from .governance_rule_setting import GovernanceRuleSetting
from .governance_rule_setting import GovernanceRuleSetting
from .governance_resource import GovernanceResource
from .governance_role_definition import GovernanceRoleDefinition

