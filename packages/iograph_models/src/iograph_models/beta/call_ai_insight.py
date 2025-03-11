from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallAiInsight(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionItems: Optional[list[ActionItem]] = Field(alias="actionItems",default=None,)
	callId: Optional[str] = Field(alias="callId",default=None,)
	contentCorrelationId: Optional[str] = Field(alias="contentCorrelationId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	meetingNotes: Optional[list[MeetingNote]] = Field(alias="meetingNotes",default=None,)
	viewpoint: Optional[CallAiInsightViewPoint] = Field(alias="viewpoint",default=None,)

from .action_item import ActionItem
from .meeting_note import MeetingNote
from .call_ai_insight_view_point import CallAiInsightViewPoint

