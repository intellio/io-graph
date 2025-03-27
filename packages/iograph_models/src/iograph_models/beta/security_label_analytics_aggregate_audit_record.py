from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityLabelAnalyticsAggregateAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.labelAnalyticsAggregateAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.labelAnalyticsAggregateAuditRecord")


