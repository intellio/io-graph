from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementPortalNotification(BaseModel):
	alertImpact: Optional[DeviceManagementAlertImpact] = Field(alias="alertImpact", default=None,)
	alertRecordId: Optional[str] = Field(alias="alertRecordId", default=None,)
	alertRuleId: Optional[str] = Field(alias="alertRuleId", default=None,)
	alertRuleName: Optional[str] = Field(alias="alertRuleName", default=None,)
	alertRuleTemplate: Optional[DeviceManagementAlertRuleTemplate | str] = Field(alias="alertRuleTemplate", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	isPortalNotificationSent: Optional[bool] = Field(alias="isPortalNotificationSent", default=None,)
	severity: Optional[DeviceManagementRuleSeverityType | str] = Field(alias="severity", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_alert_impact import DeviceManagementAlertImpact
from .device_management_alert_rule_template import DeviceManagementAlertRuleTemplate
from .device_management_rule_severity_type import DeviceManagementRuleSeverityType

