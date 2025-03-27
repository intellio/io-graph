from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsItemIdResolver(BaseModel):
	priority: Optional[int] = Field(alias="priority", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.itemIdResolver"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnectors.itemIdResolver")
	itemId: Optional[str] = Field(alias="itemId", default=None,)
	urlMatchInfo: Optional[ExternalConnectorsUrlMatchInfo] = Field(alias="urlMatchInfo", default=None,)

from .external_connectors_url_match_info import ExternalConnectorsUrlMatchInfo

