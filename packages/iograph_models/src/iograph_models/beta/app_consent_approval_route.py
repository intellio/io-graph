from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AppConsentApprovalRoute(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appConsentApprovalRoute"] = Field(alias="@odata.type",)
	appConsentRequests: Optional[list[AppConsentRequest]] = Field(alias="appConsentRequests", default=None,)

from .app_consent_request import AppConsentRequest
