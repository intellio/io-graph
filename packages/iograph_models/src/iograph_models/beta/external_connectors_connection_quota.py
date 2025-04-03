from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalConnectorsConnectionQuota(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.connectionQuota"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnectors.connectionQuota")
	itemsRemaining: Optional[int] = Field(alias="itemsRemaining", default=None,)

