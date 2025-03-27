from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesMonitoringSettings(BaseModel):
	monitoringRules: Optional[list[WindowsUpdatesMonitoringRule]] = Field(alias="monitoringRules", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_monitoring_rule import WindowsUpdatesMonitoringRule

