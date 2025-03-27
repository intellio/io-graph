from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptRemediationHistory(BaseModel):
	historyData: Optional[list[DeviceHealthScriptRemediationHistoryData]] = Field(alias="historyData", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_health_script_remediation_history_data import DeviceHealthScriptRemediationHistoryData

