from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class VppTokenRevokeLicensesActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.vppTokenRevokeLicensesActionResult"] = Field(alias="@odata.type", default="#microsoft.graph.vppTokenRevokeLicensesActionResult")
	actionFailureReason: Optional[VppTokenActionFailureReason | str] = Field(alias="actionFailureReason", default=None,)
	failedLicensesCount: Optional[int] = Field(alias="failedLicensesCount", default=None,)
	totalLicensesCount: Optional[int] = Field(alias="totalLicensesCount", default=None,)

from .action_state import ActionState
from .vpp_token_action_failure_reason import VppTokenActionFailureReason
