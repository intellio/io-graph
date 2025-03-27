from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appLogCollectionRequests: Optional[list[AppLogCollectionRequest]] = Field(alias="appLogCollectionRequests", default=None,)

from .app_log_collection_request import AppLogCollectionRequest

