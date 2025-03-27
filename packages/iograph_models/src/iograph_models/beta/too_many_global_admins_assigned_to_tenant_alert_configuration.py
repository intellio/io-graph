from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TooManyGlobalAdminsAssignedToTenantAlertConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration")
	alertDefinitionId: Optional[str] = Field(alias="alertDefinitionId", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	scopeId: Optional[str] = Field(alias="scopeId", default=None,)
	scopeType: Optional[str] = Field(alias="scopeType", default=None,)
	alertDefinition: Optional[UnifiedRoleManagementAlertDefinition] = Field(alias="alertDefinition", default=None,)
	globalAdminCountThreshold: Optional[int] = Field(alias="globalAdminCountThreshold", default=None,)
	percentageOfGlobalAdminsOutOfRolesThreshold: Optional[int] = Field(alias="percentageOfGlobalAdminsOutOfRolesThreshold", default=None,)

from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

