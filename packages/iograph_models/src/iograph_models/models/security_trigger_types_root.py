from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTriggerTypesRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	retentionEventTypes: Optional[list[SecurityRetentionEventType]] = Field(default=None,alias="retentionEventTypes",)

from .security_retention_event_type import SecurityRetentionEventType

