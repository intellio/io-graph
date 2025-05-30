from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VpnOnDemandRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VpnOnDemandRule]] = Field(alias="value", default=None,)

from .vpn_on_demand_rule import VpnOnDemandRule
