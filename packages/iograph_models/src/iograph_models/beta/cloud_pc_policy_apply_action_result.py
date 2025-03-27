from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcPolicyApplyActionResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	finishDateTime: Optional[datetime] = Field(alias="finishDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[CloudPcPolicyApplyActionStatus | str] = Field(alias="status", default=None,)

from .cloud_pc_policy_apply_action_status import CloudPcPolicyApplyActionStatus

