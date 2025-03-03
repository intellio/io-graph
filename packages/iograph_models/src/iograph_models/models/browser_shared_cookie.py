from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSharedCookie(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	comment: Optional[str] = Field(default=None,alias="comment",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	history: Optional[list[BrowserSharedCookieHistory]] = Field(default=None,alias="history",)
	hostOnly: Optional[bool] = Field(default=None,alias="hostOnly",)
	hostOrDomain: Optional[str] = Field(default=None,alias="hostOrDomain",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	path: Optional[str] = Field(default=None,alias="path",)
	sourceEnvironment: Optional[BrowserSharedCookieSourceEnvironment] = Field(default=None,alias="sourceEnvironment",)
	status: Optional[BrowserSharedCookieStatus] = Field(default=None,alias="status",)

from .browser_shared_cookie_history import BrowserSharedCookieHistory
from .identity_set import IdentitySet
from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
from .browser_shared_cookie_status import BrowserSharedCookieStatus

