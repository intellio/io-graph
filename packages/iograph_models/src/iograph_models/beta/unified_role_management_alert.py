from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlert(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alertDefinitionId: Optional[str] = Field(alias="alertDefinitionId",default=None,)
	incidentCount: Optional[int] = Field(alias="incidentCount",default=None,)
	isActive: Optional[bool] = Field(alias="isActive",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	lastScannedDateTime: Optional[datetime] = Field(alias="lastScannedDateTime",default=None,)
	scopeId: Optional[str] = Field(alias="scopeId",default=None,)
	scopeType: Optional[str] = Field(alias="scopeType",default=None,)
	alertConfiguration: SerializeAsAny[Optional[UnifiedRoleManagementAlertConfiguration]] = Field(alias="alertConfiguration",default=None,)
	alertDefinition: Optional[UnifiedRoleManagementAlertDefinition] = Field(alias="alertDefinition",default=None,)
	alertIncidents: SerializeAsAny[Optional[list[UnifiedRoleManagementAlertIncident]]] = Field(alias="alertIncidents",default=None,)

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

