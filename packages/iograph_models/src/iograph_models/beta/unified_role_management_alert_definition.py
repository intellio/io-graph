from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlertDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	howToPrevent: Optional[str] = Field(alias="howToPrevent",default=None,)
	isConfigurable: Optional[bool] = Field(alias="isConfigurable",default=None,)
	isRemediatable: Optional[bool] = Field(alias="isRemediatable",default=None,)
	mitigationSteps: Optional[str] = Field(alias="mitigationSteps",default=None,)
	scopeId: Optional[str] = Field(alias="scopeId",default=None,)
	scopeType: Optional[str] = Field(alias="scopeType",default=None,)
	securityImpact: Optional[str] = Field(alias="securityImpact",default=None,)
	severityLevel: Optional[AlertSeverity | str] = Field(alias="severityLevel",default=None,)

from .alert_severity import AlertSeverity

