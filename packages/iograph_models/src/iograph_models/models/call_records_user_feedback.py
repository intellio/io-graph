from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsUserFeedback(BaseModel):
	rating: Optional[str | CallRecordsUserFeedbackRating] = Field(alias="rating",default=None,)
	text: Optional[str] = Field(alias="text",default=None,)
	tokens: Optional[CallRecordsFeedbackTokenSet] = Field(alias="tokens",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .call_records_user_feedback_rating import CallRecordsUserFeedbackRating
from .call_records_feedback_token_set import CallRecordsFeedbackTokenSet

