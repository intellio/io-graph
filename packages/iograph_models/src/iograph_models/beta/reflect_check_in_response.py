from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ReflectCheckInResponse(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.reflectCheckInResponse"] = Field(alias="@odata.type",)
	checkInId: Optional[str] = Field(alias="checkInId", default=None,)
	checkInTitle: Optional[str] = Field(alias="checkInTitle", default=None,)
	classId: Optional[str] = Field(alias="classId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creatorId: Optional[str] = Field(alias="creatorId", default=None,)
	isClosed: Optional[bool] = Field(alias="isClosed", default=None,)
	responderId: Optional[str] = Field(alias="responderId", default=None,)
	responseEmotion: Optional[ResponseEmotionType | str] = Field(alias="responseEmotion", default=None,)
	responseFeedback: Optional[ResponseFeedbackType | str] = Field(alias="responseFeedback", default=None,)
	submitDateTime: Optional[datetime] = Field(alias="submitDateTime", default=None,)

from .response_emotion_type import ResponseEmotionType
from .response_feedback_type import ResponseFeedbackType
