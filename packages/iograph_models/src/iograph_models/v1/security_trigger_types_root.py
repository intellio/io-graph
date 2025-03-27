from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTriggerTypesRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	retentionEventTypes: Optional[list[SecurityRetentionEventType]] = Field(alias="retentionEventTypes", default=None,)

from .security_retention_event_type import SecurityRetentionEventType

