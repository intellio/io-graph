from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcPolicyApplyActionResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcPolicyApplyActionResult"] = Field(alias="@odata.type",)
	finishDateTime: Optional[datetime] = Field(alias="finishDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[CloudPcPolicyApplyActionStatus | str] = Field(alias="status", default=None,)

from .cloud_pc_policy_apply_action_status import CloudPcPolicyApplyActionStatus
