from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InviteParticipantsOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.inviteParticipantsOperation"] = Field(alias="@odata.type",)
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)
	participants: Optional[list[InvitationParticipantInfo]] = Field(alias="participants", default=None,)

from .result_info import ResultInfo
from .operation_status import OperationStatus
from .invitation_participant_info import InvitationParticipantInfo
