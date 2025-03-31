from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementAlertRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagement.alertRecord"] = Field(alias="@odata.type",)
	alertImpact: Optional[DeviceManagementAlertImpact] = Field(alias="alertImpact", default=None,)
	alertRuleId: Optional[str] = Field(alias="alertRuleId", default=None,)
	alertRuleTemplate: Optional[DeviceManagementAlertRuleTemplate | str] = Field(alias="alertRuleTemplate", default=None,)
	detectedDateTime: Optional[datetime] = Field(alias="detectedDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	resolvedDateTime: Optional[datetime] = Field(alias="resolvedDateTime", default=None,)
	severity: Optional[DeviceManagementRuleSeverityType | str] = Field(alias="severity", default=None,)
	status: Optional[DeviceManagementAlertStatusType | str] = Field(alias="status", default=None,)

from .device_management_alert_impact import DeviceManagementAlertImpact
from .device_management_alert_rule_template import DeviceManagementAlertRuleTemplate
from .device_management_rule_severity_type import DeviceManagementRuleSeverityType
from .device_management_alert_status_type import DeviceManagementAlertStatusType
