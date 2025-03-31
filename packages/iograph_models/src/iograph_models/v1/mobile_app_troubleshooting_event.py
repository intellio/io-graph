from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MobileAppTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppTroubleshootingEvent"] = Field(alias="@odata.type",)
	appLogCollectionRequests: Optional[list[AppLogCollectionRequest]] = Field(alias="appLogCollectionRequests", default=None,)

from .app_log_collection_request import AppLogCollectionRequest
