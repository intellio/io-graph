from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessTransactionSummary(BaseModel):
	blockedCount: Optional[int] = Field(alias="blockedCount",default=None,)
	totalCount: Optional[int] = Field(alias="totalCount",default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_traffic_type import NetworkaccessTrafficType

