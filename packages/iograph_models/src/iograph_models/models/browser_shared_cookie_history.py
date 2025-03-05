from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSharedCookieHistory(BaseModel):
	comment: Optional[str] = Field(alias="comment",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	hostOnly: Optional[bool] = Field(alias="hostOnly",default=None,)
	hostOrDomain: Optional[str] = Field(alias="hostOrDomain",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	path: Optional[str] = Field(alias="path",default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime",default=None,)
	sourceEnvironment: Optional[BrowserSharedCookieSourceEnvironment | str] = Field(alias="sourceEnvironment",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment

