from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSharedCookie(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	comment: Optional[str] = Field(alias="comment",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	history: Optional[list[BrowserSharedCookieHistory]] = Field(alias="history",default=None,)
	hostOnly: Optional[bool] = Field(alias="hostOnly",default=None,)
	hostOrDomain: Optional[str] = Field(alias="hostOrDomain",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	path: Optional[str] = Field(alias="path",default=None,)
	sourceEnvironment: Optional[BrowserSharedCookieSourceEnvironment | str] = Field(alias="sourceEnvironment",default=None,)
	status: Optional[BrowserSharedCookieStatus | str] = Field(alias="status",default=None,)

from .browser_shared_cookie_history import BrowserSharedCookieHistory
from .identity_set import IdentitySet
from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
from .browser_shared_cookie_status import BrowserSharedCookieStatus

