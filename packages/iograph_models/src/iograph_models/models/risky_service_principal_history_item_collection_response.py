from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RiskyServicePrincipalHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[RiskyServicePrincipalHistoryItem]] = Field(default=None,alias="value",)

from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem

