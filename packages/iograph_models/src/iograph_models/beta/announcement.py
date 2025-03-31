from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Announcement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.announcement"] = Field(alias="@odata.type", default="#microsoft.graph.announcement")
	changeItemService: Optional[str] = Field(alias="changeItemService", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	documentationUrls: Optional[list[str]] = Field(alias="documentationUrls", default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription", default=None,)
	systemTags: Optional[list[str]] = Field(alias="systemTags", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	announcementDateTime: Optional[datetime] = Field(alias="announcementDateTime", default=None,)
	changeType: Optional[ChangeAnnouncementChangeType | str] = Field(alias="changeType", default=None,)
	impactLink: Optional[str] = Field(alias="impactLink", default=None,)
	isCustomerActionRequired: Optional[bool] = Field(alias="isCustomerActionRequired", default=None,)
	targetDateTime: Optional[datetime] = Field(alias="targetDateTime", default=None,)

from .change_announcement_change_type import ChangeAnnouncementChangeType
