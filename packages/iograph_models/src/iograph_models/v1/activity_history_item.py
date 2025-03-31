from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ActivityHistoryItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.activityHistoryItem"] = Field(alias="@odata.type",)
	activeDurationSeconds: Optional[int] = Field(alias="activeDurationSeconds", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastActiveDateTime: Optional[datetime] = Field(alias="lastActiveDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime", default=None,)
	status: Optional[Status | str] = Field(alias="status", default=None,)
	userTimezone: Optional[str] = Field(alias="userTimezone", default=None,)
	activity: Optional[UserActivity] = Field(alias="activity", default=None,)

from .status import Status
from .user_activity import UserActivity
