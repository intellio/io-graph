from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityRetentionEventTypeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityRetentionEventType] = Field(alias="value",)

from .security_retention_event_type import SecurityRetentionEventType

