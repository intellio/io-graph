from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCdpLogRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpLogRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpLogRecord")

