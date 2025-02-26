from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InvitationParticipantInfo(BaseModel):
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	identity: Optional[IdentitySet] = Field(default=None,alias="identity",)
	participantId: Optional[str] = Field(default=None,alias="participantId",)
	removeFromDefaultAudioRoutingGroup: Optional[bool] = Field(default=None,alias="removeFromDefaultAudioRoutingGroup",)
	replacesCallId: Optional[str] = Field(default=None,alias="replacesCallId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

