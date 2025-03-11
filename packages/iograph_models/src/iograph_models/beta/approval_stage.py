from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalStage(BaseModel):
	approvalStageTimeOutInDays: Optional[int] = Field(alias="approvalStageTimeOutInDays",default=None,)
	escalationApprovers: SerializeAsAny[Optional[list[UserSet]]] = Field(alias="escalationApprovers",default=None,)
	escalationTimeInMinutes: Optional[int] = Field(alias="escalationTimeInMinutes",default=None,)
	isApproverJustificationRequired: Optional[bool] = Field(alias="isApproverJustificationRequired",default=None,)
	isEscalationEnabled: Optional[bool] = Field(alias="isEscalationEnabled",default=None,)
	primaryApprovers: SerializeAsAny[Optional[list[UserSet]]] = Field(alias="primaryApprovers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .user_set import UserSet
from .user_set import UserSet

