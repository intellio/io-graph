from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_scheduled_actionsPostRequest(BaseModel):
	scheduledActions: Optional[list[DeviceManagementComplianceScheduledActionForRule]] = Field(alias="scheduledActions", default=None,)

from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
