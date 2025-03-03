from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventRegistrationQuestionBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[VirtualEventRegistrationQuestionBase]] = Field(default=None,alias="value",)

from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

