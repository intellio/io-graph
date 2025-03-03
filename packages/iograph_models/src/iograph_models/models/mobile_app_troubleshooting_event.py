from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileAppTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appLogCollectionRequests: Optional[list[AppLogCollectionRequest]] = Field(default=None,alias="appLogCollectionRequests",)

from .app_log_collection_request import AppLogCollectionRequest

