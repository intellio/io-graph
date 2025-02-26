from __future__ import annotations
from pydantic import BaseModel, Field


class Schedule_actions_for_rulesPostRequest(BaseModel):
	deviceComplianceScheduledActionForRules: list[DeviceComplianceScheduledActionForRule] = Field(alias="deviceComplianceScheduledActionForRules",)

from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

