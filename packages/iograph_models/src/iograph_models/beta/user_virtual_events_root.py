from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserVirtualEventsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userVirtualEventsRoot"] = Field(alias="@odata.type",)
	webinars: Optional[list[VirtualEventWebinar]] = Field(alias="webinars", default=None,)

from .virtual_event_webinar import VirtualEventWebinar
