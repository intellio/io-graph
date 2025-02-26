from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileThreatDefenseConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MobileThreatDefenseConnector] = Field(alias="value",)

from .mobile_threat_defense_connector import MobileThreatDefenseConnector

