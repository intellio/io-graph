from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppConsentRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	pendingScopes: list[AppConsentRequestScope] = Field(alias="pendingScopes",)
	userConsentRequests: list[UserConsentRequest] = Field(alias="userConsentRequests",)

from .app_consent_request_scope import AppConsentRequestScope
from .user_consent_request import UserConsentRequest

