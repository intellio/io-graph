from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityTriggersRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.triggersRoot"] = Field(alias="@odata.type", default="#microsoft.graph.security.triggersRoot")
	retentionEvents: Optional[list[SecurityRetentionEvent]] = Field(alias="retentionEvents", default=None,)

from .security_retention_event import SecurityRetentionEvent
