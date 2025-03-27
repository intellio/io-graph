from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelSimulationSharePointCompletionRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelSimulationSharePointCompletionRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelSimulationSharePointCompletionRecord")


