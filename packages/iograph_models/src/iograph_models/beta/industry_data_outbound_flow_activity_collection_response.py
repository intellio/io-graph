from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataOutboundFlowActivityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IndustryDataOutboundFlowActivity]] = Field(alias="value", default=None,)

from .industry_data_outbound_flow_activity import IndustryDataOutboundFlowActivity
