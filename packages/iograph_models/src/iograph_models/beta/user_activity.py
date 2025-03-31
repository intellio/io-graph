from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userActivity"] = Field(alias="@odata.type",)
	activationUrl: Optional[str] = Field(alias="activationUrl", default=None,)
	activitySourceHost: Optional[str] = Field(alias="activitySourceHost", default=None,)
	appActivityId: Optional[str] = Field(alias="appActivityId", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	contentInfo: Optional[str] = Field(alias="contentInfo", default=None,)
	contentUrl: Optional[str] = Field(alias="contentUrl", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	fallbackUrl: Optional[str] = Field(alias="fallbackUrl", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[Status | str] = Field(alias="status", default=None,)
	userTimezone: Optional[str] = Field(alias="userTimezone", default=None,)
	visualElements: Optional[VisualInfo] = Field(alias="visualElements", default=None,)
	historyItems: Optional[list[ActivityHistoryItem]] = Field(alias="historyItems", default=None,)

from .status import Status
from .visual_info import VisualInfo
from .activity_history_item import ActivityHistoryItem
