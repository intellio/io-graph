from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRetentionDurationInDays(BaseModel):
	odata_type: Literal["#microsoft.graph.security.retentionDurationInDays"] = Field(alias="@odata.type", default="#microsoft.graph.security.retentionDurationInDays")
	days: Optional[int] = Field(alias="days", default=None,)


