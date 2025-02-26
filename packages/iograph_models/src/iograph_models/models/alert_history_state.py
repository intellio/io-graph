from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AlertHistoryState(BaseModel):
	appId: Optional[str] = Field(default=None,alias="appId",)
	assignedTo: Optional[str] = Field(default=None,alias="assignedTo",)
	comments: list[Optional[str]] = Field(alias="comments",)
	feedback: Optional[AlertFeedback] = Field(default=None,alias="feedback",)
	status: Optional[AlertStatus] = Field(default=None,alias="status",)
	updatedDateTime: Optional[datetime] = Field(default=None,alias="updatedDateTime",)
	user: Optional[str] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .alert_feedback import AlertFeedback
from .alert_status import AlertStatus

