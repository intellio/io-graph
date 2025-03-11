from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppConsentApprovalRoute(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appConsentRequests: Optional[list[AppConsentRequest]] = Field(alias="appConsentRequests",default=None,)

from .app_consent_request import AppConsentRequest

