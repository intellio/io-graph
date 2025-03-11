from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementAlertRule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alertRuleTemplate: Optional[DeviceManagementAlertRuleTemplate | str] = Field(alias="alertRuleTemplate",default=None,)
	conditions: Optional[list[DeviceManagementRuleCondition]] = Field(alias="conditions",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	isSystemRule: Optional[bool] = Field(alias="isSystemRule",default=None,)
	notificationChannels: Optional[list[DeviceManagementNotificationChannel]] = Field(alias="notificationChannels",default=None,)
	severity: Optional[DeviceManagementRuleSeverityType | str] = Field(alias="severity",default=None,)
	threshold: Optional[DeviceManagementRuleThreshold] = Field(alias="threshold",default=None,)

from .device_management_alert_rule_template import DeviceManagementAlertRuleTemplate
from .device_management_rule_condition import DeviceManagementRuleCondition
from .device_management_notification_channel import DeviceManagementNotificationChannel
from .device_management_rule_severity_type import DeviceManagementRuleSeverityType
from .device_management_rule_threshold import DeviceManagementRuleThreshold

