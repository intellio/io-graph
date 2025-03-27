from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipLabelAnalyticsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipLabelAnalyticsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipLabelAnalyticsAuditRecord")


