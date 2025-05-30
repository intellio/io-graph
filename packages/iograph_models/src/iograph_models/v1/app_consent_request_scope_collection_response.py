from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppConsentRequestScopeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AppConsentRequestScope]] = Field(alias="value", default=None,)

from .app_consent_request_scope import AppConsentRequestScope
