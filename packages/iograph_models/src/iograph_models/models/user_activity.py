from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserActivity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activationUrl: Optional[str] = Field(default=None,alias="activationUrl",)
	activitySourceHost: Optional[str] = Field(default=None,alias="activitySourceHost",)
	appActivityId: Optional[str] = Field(default=None,alias="appActivityId",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	contentInfo: Optional[str] = Field(default=None,alias="contentInfo",)
	contentUrl: Optional[str] = Field(default=None,alias="contentUrl",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	fallbackUrl: Optional[str] = Field(default=None,alias="fallbackUrl",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[Status] = Field(default=None,alias="status",)
	userTimezone: Optional[str] = Field(default=None,alias="userTimezone",)
	visualElements: Optional[VisualInfo] = Field(default=None,alias="visualElements",)
	historyItems: list[ActivityHistoryItem] = Field(alias="historyItems",)

from .status import Status
from .visual_info import VisualInfo
from .activity_history_item import ActivityHistoryItem

