from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RiskyServicePrincipalHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[RiskyServicePrincipalHistoryItem]] = Field(alias="value", default=None,)

from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
