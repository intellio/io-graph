from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdatesMonitoringRule(BaseModel):
	action: Optional[WindowsUpdatesMonitoringAction | str] = Field(alias="action", default=None,)
	signal: Optional[WindowsUpdatesMonitoringSignal | str] = Field(alias="signal", default=None,)
	threshold: Optional[int] = Field(alias="threshold", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_monitoring_action import WindowsUpdatesMonitoringAction
from .windows_updates_monitoring_signal import WindowsUpdatesMonitoringSignal
