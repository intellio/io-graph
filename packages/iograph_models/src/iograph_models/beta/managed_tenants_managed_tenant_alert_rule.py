from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantAlertRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	alertDisplayName: Optional[str] = Field(alias="alertDisplayName", default=None,)
	alertTTL: Optional[int] = Field(alias="alertTTL", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	lastRunDateTime: Optional[datetime] = Field(alias="lastRunDateTime", default=None,)
	notificationFinalDestinations: Optional[ManagedTenantsNotificationDestination | str] = Field(alias="notificationFinalDestinations", default=None,)
	severity: Optional[ManagedTenantsAlertSeverity | str] = Field(alias="severity", default=None,)
	targets: Optional[list[ManagedTenantsNotificationTarget]] = Field(alias="targets", default=None,)
	tenantIds: Optional[list[ManagedTenantsTenantInfo]] = Field(alias="tenantIds", default=None,)
	alerts: Optional[list[ManagedTenantsManagedTenantAlert]] = Field(alias="alerts", default=None,)
	ruleDefinition: Optional[ManagedTenantsManagedTenantAlertRuleDefinition] = Field(alias="ruleDefinition", default=None,)

from .managed_tenants_notification_destination import ManagedTenantsNotificationDestination
from .managed_tenants_alert_severity import ManagedTenantsAlertSeverity
from .managed_tenants_notification_target import ManagedTenantsNotificationTarget
from .managed_tenants_tenant_info import ManagedTenantsTenantInfo
from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert
from .managed_tenants_managed_tenant_alert_rule_definition import ManagedTenantsManagedTenantAlertRuleDefinition

