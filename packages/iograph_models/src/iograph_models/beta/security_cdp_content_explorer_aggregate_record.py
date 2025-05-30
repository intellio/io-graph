from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCdpContentExplorerAggregateRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpContentExplorerAggregateRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpContentExplorerAggregateRecord")

