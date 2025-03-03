from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PublishPostRequest(BaseModel):
	revision: Optional[str] = Field(default=None,alias="revision",)
	sites: Optional[list[BrowserSite]] = Field(default=None,alias="sites",)
	sharedCookies: Optional[list[BrowserSharedCookie]] = Field(default=None,alias="sharedCookies",)

from .browser_site import BrowserSite
from .browser_shared_cookie import BrowserSharedCookie

