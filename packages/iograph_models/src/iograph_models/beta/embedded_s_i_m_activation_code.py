from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmbeddedSIMActivationCode(BaseModel):
	integratedCircuitCardIdentifier: Optional[str] = Field(alias="integratedCircuitCardIdentifier", default=None,)
	matchingIdentifier: Optional[str] = Field(alias="matchingIdentifier", default=None,)
	smdpPlusServerAddress: Optional[str] = Field(alias="smdpPlusServerAddress", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

