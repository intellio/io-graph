from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppConsentApprovalRoute(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appConsentRequests: Optional[list[AppConsentRequest]] = Field(default=None,alias="appConsentRequests",)

from .app_consent_request import AppConsentRequest

