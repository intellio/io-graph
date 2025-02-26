from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnmuteParticipantOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UnmuteParticipantOperation] = Field(alias="value",)

from .unmute_participant_operation import UnmuteParticipantOperation

