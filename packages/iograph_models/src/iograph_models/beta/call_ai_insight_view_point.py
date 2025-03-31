from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallAiInsightViewPoint(BaseModel):
	mentionEvents: Optional[list[MentionEvent]] = Field(alias="mentionEvents", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .mention_event import MentionEvent
