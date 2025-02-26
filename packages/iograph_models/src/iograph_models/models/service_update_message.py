from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceUpdateMessage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	details: list[KeyValuePair] = Field(alias="details",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	title: Optional[str] = Field(default=None,alias="title",)
	actionRequiredByDateTime: Optional[datetime] = Field(default=None,alias="actionRequiredByDateTime",)
	attachmentsArchive: Optional[str] = Field(default=None,alias="attachmentsArchive",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	category: Optional[ServiceUpdateCategory] = Field(default=None,alias="category",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	isMajorChange: Optional[bool] = Field(default=None,alias="isMajorChange",)
	services: list[Optional[str]] = Field(alias="services",)
	severity: Optional[ServiceUpdateSeverity] = Field(default=None,alias="severity",)
	tags: list[Optional[str]] = Field(alias="tags",)
	viewPoint: Optional[ServiceUpdateMessageViewpoint] = Field(default=None,alias="viewPoint",)
	attachments: list[ServiceAnnouncementAttachment] = Field(alias="attachments",)

from .key_value_pair import KeyValuePair
from .item_body import ItemBody
from .service_update_category import ServiceUpdateCategory
from .service_update_severity import ServiceUpdateSeverity
from .service_update_message_viewpoint import ServiceUpdateMessageViewpoint
from .service_announcement_attachment import ServiceAnnouncementAttachment

