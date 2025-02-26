from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TransferPostRequest(BaseModel):
	transferTarget: Optional[InvitationParticipantInfo] = Field(default=None,alias="transferTarget",)
	transferee: Optional[ParticipantInfo] = Field(default=None,alias="transferee",)

from .invitation_participant_info import InvitationParticipantInfo
from .participant_info import ParticipantInfo

