from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsUserFeedback(BaseModel):
	rating: Optional[CallRecordsUserFeedbackRating] = Field(default=None,alias="rating",)
	text: Optional[str] = Field(default=None,alias="text",)
	tokens: Optional[CallRecordsFeedbackTokenSet] = Field(default=None,alias="tokens",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_user_feedback_rating import CallRecordsUserFeedbackRating
from .call_records_feedback_token_set import CallRecordsFeedbackTokenSet

