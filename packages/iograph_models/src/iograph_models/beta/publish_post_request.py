from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PublishPostRequest(BaseModel):
	revision: Optional[str] = Field(alias="revision", default=None,)
	sites: Optional[list[BrowserSite]] = Field(alias="sites", default=None,)
	sharedCookies: Optional[list[BrowserSharedCookie]] = Field(alias="sharedCookies", default=None,)

from .browser_site import BrowserSite
from .browser_shared_cookie import BrowserSharedCookie
