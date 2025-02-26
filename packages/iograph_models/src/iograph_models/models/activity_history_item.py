from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ActivityHistoryItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeDurationSeconds: Optional[int] = Field(default=None,alias="activeDurationSeconds",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	lastActiveDateTime: Optional[datetime] = Field(default=None,alias="lastActiveDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	startedDateTime: Optional[datetime] = Field(default=None,alias="startedDateTime",)
	status: Optional[Status] = Field(default=None,alias="status",)
	userTimezone: Optional[str] = Field(default=None,alias="userTimezone",)
	activity: Optional[UserActivity] = Field(default=None,alias="activity",)

from .status import Status
from .user_activity import UserActivity

