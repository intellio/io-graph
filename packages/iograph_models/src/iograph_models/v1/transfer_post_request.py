from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TransferPostRequest(BaseModel):
	transferTarget: Optional[InvitationParticipantInfo] = Field(alias="transferTarget", default=None,)
	transferee: Optional[ParticipantInfo] = Field(alias="transferee", default=None,)

from .invitation_participant_info import InvitationParticipantInfo
from .participant_info import ParticipantInfo

