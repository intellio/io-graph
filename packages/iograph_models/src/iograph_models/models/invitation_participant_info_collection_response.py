from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InvitationParticipantInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[InvitationParticipantInfo]] = Field(default=None,alias="value",)

from .invitation_participant_info import InvitationParticipantInfo

