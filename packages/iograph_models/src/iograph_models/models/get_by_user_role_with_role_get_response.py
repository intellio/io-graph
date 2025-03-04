from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_by_user_role_with_roleGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[VirtualEventWebinar]] = Field(default=None,alias="value",)

from .virtual_event_webinar import VirtualEventWebinar

