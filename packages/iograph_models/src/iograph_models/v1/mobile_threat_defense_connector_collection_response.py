from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileThreatDefenseConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MobileThreatDefenseConnector]] = Field(alias="value", default=None,)

from .mobile_threat_defense_connector import MobileThreatDefenseConnector
