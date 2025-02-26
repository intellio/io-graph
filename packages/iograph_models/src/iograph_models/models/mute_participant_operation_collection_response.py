from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MuteParticipantOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MuteParticipantOperation] = Field(alias="value",)

from .mute_participant_operation import MuteParticipantOperation

