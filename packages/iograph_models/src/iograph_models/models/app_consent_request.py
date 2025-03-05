from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppConsentRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	pendingScopes: Optional[list[AppConsentRequestScope]] = Field(default=None,alias="pendingScopes",)
	userConsentRequests: Optional[list[UserConsentRequest]] = Field(default=None,alias="userConsentRequests",)

from .app_consent_request_scope import AppConsentRequestScope
from .user_consent_request import UserConsentRequest

