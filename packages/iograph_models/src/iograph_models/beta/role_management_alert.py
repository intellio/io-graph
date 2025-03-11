from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoleManagementAlert(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alertConfigurations: SerializeAsAny[Optional[list[UnifiedRoleManagementAlertConfiguration]]] = Field(alias="alertConfigurations",default=None,)
	alertDefinitions: Optional[list[UnifiedRoleManagementAlertDefinition]] = Field(alias="alertDefinitions",default=None,)
	alerts: Optional[list[UnifiedRoleManagementAlert]] = Field(alias="alerts",default=None,)
	operations: SerializeAsAny[Optional[list[LongRunningOperation]]] = Field(alias="operations",default=None,)

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
from .unified_role_management_alert import UnifiedRoleManagementAlert
from .long_running_operation import LongRunningOperation

