from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSharedCookieHistory(BaseModel):
	comment: Optional[str] = Field(default=None,alias="comment",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	hostOnly: Optional[bool] = Field(default=None,alias="hostOnly",)
	hostOrDomain: Optional[str] = Field(default=None,alias="hostOrDomain",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	path: Optional[str] = Field(default=None,alias="path",)
	publishedDateTime: Optional[datetime] = Field(default=None,alias="publishedDateTime",)
	sourceEnvironment: Optional[BrowserSharedCookieSourceEnvironment] = Field(default=None,alias="sourceEnvironment",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment

