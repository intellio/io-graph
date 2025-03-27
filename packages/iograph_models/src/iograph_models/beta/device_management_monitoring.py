from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementMonitoring(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	alertRecords: Optional[list[DeviceManagementAlertRecord]] = Field(alias="alertRecords", default=None,)
	alertRules: Optional[list[DeviceManagementAlertRule]] = Field(alias="alertRules", default=None,)

from .device_management_alert_record import DeviceManagementAlertRecord
from .device_management_alert_rule import DeviceManagementAlertRule

