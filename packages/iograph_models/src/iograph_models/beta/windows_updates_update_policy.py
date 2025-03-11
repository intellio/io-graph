from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdatePolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	complianceChangeRules: SerializeAsAny[Optional[list[WindowsUpdatesComplianceChangeRule]]] = Field(alias="complianceChangeRules",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deploymentSettings: Optional[WindowsUpdatesDeploymentSettings] = Field(alias="deploymentSettings",default=None,)
	audience: Optional[WindowsUpdatesDeploymentAudience] = Field(alias="audience",default=None,)
	complianceChanges: SerializeAsAny[Optional[list[WindowsUpdatesComplianceChange]]] = Field(alias="complianceChanges",default=None,)

from .windows_updates_compliance_change_rule import WindowsUpdatesComplianceChangeRule
from .windows_updates_deployment_settings import WindowsUpdatesDeploymentSettings
from .windows_updates_deployment_audience import WindowsUpdatesDeploymentAudience
from .windows_updates_compliance_change import WindowsUpdatesComplianceChange

