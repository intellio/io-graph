from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityRetentionDurationForever(BaseModel):
	odata_type: Literal["#microsoft.graph.security.retentionDurationForever"] = Field(alias="@odata.type", default="#microsoft.graph.security.retentionDurationForever")

