from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementMonitoring(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagement.monitoring"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagement.monitoring")
	alertRecords: Optional[list[DeviceManagementAlertRecord]] = Field(alias="alertRecords", default=None,)
	alertRules: Optional[list[DeviceManagementAlertRule]] = Field(alias="alertRules", default=None,)

from .device_management_alert_record import DeviceManagementAlertRecord
from .device_management_alert_rule import DeviceManagementAlertRule
