from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MacOsVppAppRevokeLicensesActionResult(BaseModel):
	actionFailureReason: Optional[VppTokenActionFailureReason | str] = Field(alias="actionFailureReason", default=None,)
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState", default=None,)
	failedLicensesCount: Optional[int] = Field(alias="failedLicensesCount", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	totalLicensesCount: Optional[int] = Field(alias="totalLicensesCount", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .vpp_token_action_failure_reason import VppTokenActionFailureReason
from .action_state import ActionState
