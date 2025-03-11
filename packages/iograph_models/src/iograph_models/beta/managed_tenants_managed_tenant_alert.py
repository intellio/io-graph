from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantAlert(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alertData: Optional[ManagedTenantsAlertData] = Field(alias="alertData",default=None,)
	alertDataReferenceStrings: Optional[list[ManagedTenantsAlertDataReferenceString]] = Field(alias="alertDataReferenceStrings",default=None,)
	alertRuleDisplayName: Optional[str] = Field(alias="alertRuleDisplayName",default=None,)
	assignedToUserId: Optional[str] = Field(alias="assignedToUserId",default=None,)
	correlationCount: Optional[int] = Field(alias="correlationCount",default=None,)
	correlationId: Optional[str] = Field(alias="correlationId",default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	message: Optional[str] = Field(alias="message",default=None,)
	severity: Optional[ManagedTenantsAlertSeverity | str] = Field(alias="severity",default=None,)
	status: Optional[ManagedTenantsAlertStatus | str] = Field(alias="status",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	alertLogs: Optional[list[ManagedTenantsManagedTenantAlertLog]] = Field(alias="alertLogs",default=None,)
	alertRule: Optional[ManagedTenantsManagedTenantAlertRule] = Field(alias="alertRule",default=None,)
	apiNotifications: Optional[list[ManagedTenantsManagedTenantApiNotification]] = Field(alias="apiNotifications",default=None,)
	emailNotifications: Optional[list[ManagedTenantsManagedTenantEmailNotification]] = Field(alias="emailNotifications",default=None,)

from .managed_tenants_alert_data import ManagedTenantsAlertData
from .managed_tenants_alert_data_reference_string import ManagedTenantsAlertDataReferenceString
from .managed_tenants_alert_severity import ManagedTenantsAlertSeverity
from .managed_tenants_alert_status import ManagedTenantsAlertStatus
from .managed_tenants_managed_tenant_alert_log import ManagedTenantsManagedTenantAlertLog
from .managed_tenants_managed_tenant_alert_rule import ManagedTenantsManagedTenantAlertRule
from .managed_tenants_managed_tenant_api_notification import ManagedTenantsManagedTenantApiNotification
from .managed_tenants_managed_tenant_email_notification import ManagedTenantsManagedTenantEmailNotification

