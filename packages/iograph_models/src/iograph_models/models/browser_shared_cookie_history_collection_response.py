from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSharedCookieHistoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[BrowserSharedCookieHistory]] = Field(default=None,alias="value",)

from .browser_shared_cookie_history import BrowserSharedCookieHistory

