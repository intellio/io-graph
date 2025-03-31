from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPowerPlatformLockboxResourceCommandAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerPlatformLockboxResourceCommandAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerPlatformLockboxResourceCommandAuditRecord")

