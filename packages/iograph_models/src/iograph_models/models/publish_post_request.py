from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PublishPostRequest(BaseModel):
	revision: Optional[str] = Field(default=None,alias="revision",)
	sites: list[BrowserSite] = Field(alias="sites",)
	sharedCookies: list[BrowserSharedCookie] = Field(alias="sharedCookies",)

from .browser_site import BrowserSite
from .browser_shared_cookie import BrowserSharedCookie

