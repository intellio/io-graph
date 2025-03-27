from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Schedule_policy_apply_taskPostRequest(BaseModel):
	scheduledRule: Optional[CloudPcPolicyScheduledApplyActionDetail] = Field(alias="scheduledRule", default=None,)

from .cloud_pc_policy_scheduled_apply_action_detail import CloudPcPolicyScheduledApplyActionDetail

