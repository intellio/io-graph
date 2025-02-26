from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventRegistrationQuestionAnswerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[VirtualEventRegistrationQuestionAnswer] = Field(alias="value",)

from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer

