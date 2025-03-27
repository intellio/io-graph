from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AlertHistoryState(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	comments: Optional[list[str]] = Field(alias="comments", default=None,)
	feedback: Optional[AlertFeedback | str] = Field(alias="feedback", default=None,)
	status: Optional[AlertStatus | str] = Field(alias="status", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	user: Optional[str] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .alert_feedback import AlertFeedback
from .alert_status import AlertStatus

