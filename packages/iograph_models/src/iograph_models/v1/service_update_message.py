from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceUpdateMessage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceUpdateMessage"] = Field(alias="@odata.type", default="#microsoft.graph.serviceUpdateMessage")
	details: Optional[list[KeyValuePair]] = Field(alias="details", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	actionRequiredByDateTime: Optional[datetime] = Field(alias="actionRequiredByDateTime", default=None,)
	attachmentsArchive: Optional[str] = Field(alias="attachmentsArchive", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	category: Optional[ServiceUpdateCategory | str] = Field(alias="category", default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	isMajorChange: Optional[bool] = Field(alias="isMajorChange", default=None,)
	services: Optional[list[str]] = Field(alias="services", default=None,)
	severity: Optional[ServiceUpdateSeverity | str] = Field(alias="severity", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	viewPoint: Optional[ServiceUpdateMessageViewpoint] = Field(alias="viewPoint", default=None,)
	attachments: Optional[list[ServiceAnnouncementAttachment]] = Field(alias="attachments", default=None,)

from .key_value_pair import KeyValuePair
from .item_body import ItemBody
from .service_update_category import ServiceUpdateCategory
from .service_update_severity import ServiceUpdateSeverity
from .service_update_message_viewpoint import ServiceUpdateMessageViewpoint
from .service_announcement_attachment import ServiceAnnouncementAttachment
