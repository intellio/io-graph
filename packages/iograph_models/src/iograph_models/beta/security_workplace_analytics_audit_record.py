from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWorkplaceAnalyticsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.workplaceAnalyticsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.workplaceAnalyticsAuditRecord")


