from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditEventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AuditEvent] = Field(alias="value",)

from .audit_event import AuditEvent

