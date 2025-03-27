from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelSimulationSharePointProgressRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelSimulationSharePointProgressRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelSimulationSharePointProgressRecord")


