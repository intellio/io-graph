from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelSimulationStatisticsRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelSimulationStatisticsRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelSimulationStatisticsRecord")


