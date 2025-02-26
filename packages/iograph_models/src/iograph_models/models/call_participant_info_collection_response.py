from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallParticipantInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CallParticipantInfo] = Field(alias="value",)

from .call_participant_info import CallParticipantInfo

