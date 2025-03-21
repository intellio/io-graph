from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StaleSignInAlertConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alertDefinitionId: Optional[str] = Field(alias="alertDefinitionId",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	scopeId: Optional[str] = Field(alias="scopeId",default=None,)
	scopeType: Optional[str] = Field(alias="scopeType",default=None,)
	alertDefinition: Optional[UnifiedRoleManagementAlertDefinition] = Field(alias="alertDefinition",default=None,)
	duration: Optional[str] = Field(alias="duration",default=None,)

from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

