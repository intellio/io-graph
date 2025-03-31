from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AppConsentRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appConsentRequest"] = Field(alias="@odata.type",)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	consentType: Optional[str] = Field(alias="consentType", default=None,)
	pendingScopes: Optional[list[AppConsentRequestScope]] = Field(alias="pendingScopes", default=None,)
	userConsentRequests: Optional[list[UserConsentRequest]] = Field(alias="userConsentRequests", default=None,)

from .app_consent_request_scope import AppConsentRequestScope
from .user_consent_request import UserConsentRequest
