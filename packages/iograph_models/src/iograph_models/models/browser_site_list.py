from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSiteList(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publishedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="publishedBy",default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime",default=None,)
	revision: Optional[str] = Field(alias="revision",default=None,)
	status: Optional[str | BrowserSiteListStatus] = Field(alias="status",default=None,)
	sharedCookies: Optional[list[BrowserSharedCookie]] = Field(alias="sharedCookies",default=None,)
	sites: Optional[list[BrowserSite]] = Field(alias="sites",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .browser_site_list_status import BrowserSiteListStatus
from .browser_shared_cookie import BrowserSharedCookie
from .browser_site import BrowserSite

