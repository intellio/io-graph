from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserVirtualEventsRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	webinars: Optional[list[VirtualEventWebinar]] = Field(alias="webinars",default=None,)

from .virtual_event_webinar import VirtualEventWebinar

