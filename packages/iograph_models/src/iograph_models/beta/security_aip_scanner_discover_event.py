from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAipScannerDiscoverEvent(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aipScannerDiscoverEvent"] = Field(alias="@odata.type", default="#microsoft.graph.security.aipScannerDiscoverEvent")

