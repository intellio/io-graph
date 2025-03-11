from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppConsentRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	pendingScopes: Optional[list[AppConsentRequestScope]] = Field(alias="pendingScopes",default=None,)
	userConsentRequests: Optional[list[UserConsentRequest]] = Field(alias="userConsentRequests",default=None,)

from .app_consent_request_scope import AppConsentRequestScope
from .user_consent_request import UserConsentRequest

