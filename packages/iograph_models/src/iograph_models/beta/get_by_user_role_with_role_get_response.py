from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_by_user_role_with_roleGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VirtualEventWebinar]] = Field(alias="value", default=None,)

from .virtual_event_webinar import VirtualEventWebinar
