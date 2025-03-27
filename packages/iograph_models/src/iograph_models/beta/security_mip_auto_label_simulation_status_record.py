from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelSimulationStatusRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelSimulationStatusRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelSimulationStatusRecord")


