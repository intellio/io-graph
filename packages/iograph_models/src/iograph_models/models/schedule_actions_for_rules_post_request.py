from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Schedule_actions_for_rulesPostRequest(BaseModel):
	deviceComplianceScheduledActionForRules: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(default=None,alias="deviceComplianceScheduledActionForRules",)

from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

