from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceAnnouncementAttachmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ServiceAnnouncementAttachment]] = Field(alias="value", default=None,)

from .service_announcement_attachment import ServiceAnnouncementAttachment
