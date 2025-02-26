from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcAuditEventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudPcAuditEvent] = Field(alias="value",)

from .cloud_pc_audit_event import CloudPcAuditEvent

