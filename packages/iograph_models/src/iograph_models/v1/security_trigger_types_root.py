from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityTriggerTypesRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.triggerTypesRoot"] = Field(alias="@odata.type",)
	retentionEventTypes: Optional[list[SecurityRetentionEventType]] = Field(alias="retentionEventTypes", default=None,)

from .security_retention_event_type import SecurityRetentionEventType
