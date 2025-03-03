from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnUserCreateStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OnUserCreateStartListener]] = Field(default=None,alias="value",)

from .on_user_create_start_listener import OnUserCreateStartListener

