from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPowerPlatformLockboxResourceAccessRequestAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerPlatformLockboxResourceAccessRequestAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerPlatformLockboxResourceAccessRequestAuditRecord")


