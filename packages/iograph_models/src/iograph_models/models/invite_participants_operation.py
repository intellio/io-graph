from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InviteParticipantsOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[OperationStatus] = Field(default=None,alias="status",)
	participants: Optional[list[InvitationParticipantInfo]] = Field(default=None,alias="participants",)

from .result_info import ResultInfo
from .operation_status import OperationStatus
from .invitation_participant_info import InvitationParticipantInfo

