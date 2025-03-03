from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSiteList(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	publishedBy: Optional[IdentitySet] = Field(default=None,alias="publishedBy",)
	publishedDateTime: Optional[datetime] = Field(default=None,alias="publishedDateTime",)
	revision: Optional[str] = Field(default=None,alias="revision",)
	status: Optional[BrowserSiteListStatus] = Field(default=None,alias="status",)
	sharedCookies: Optional[list[BrowserSharedCookie]] = Field(default=None,alias="sharedCookies",)
	sites: Optional[list[BrowserSite]] = Field(default=None,alias="sites",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .browser_site_list_status import BrowserSiteListStatus
from .browser_shared_cookie import BrowserSharedCookie
from .browser_site import BrowserSite

