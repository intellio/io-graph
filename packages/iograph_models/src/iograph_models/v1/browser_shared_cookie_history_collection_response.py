from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSharedCookieHistoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[BrowserSharedCookieHistory]] = Field(alias="value", default=None,)

from .browser_shared_cookie_history import BrowserSharedCookieHistory

