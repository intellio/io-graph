from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityExchangeAggregatedOperationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.exchangeAggregatedOperationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.exchangeAggregatedOperationRecord")

