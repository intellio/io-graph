from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsItemIdResolver(BaseModel):
	priority: Optional[int] = Field(default=None,alias="priority",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	itemId: Optional[str] = Field(default=None,alias="itemId",)
	urlMatchInfo: Optional[ExternalConnectorsUrlMatchInfo] = Field(default=None,alias="urlMatchInfo",)

from .external_connectors_url_match_info import ExternalConnectorsUrlMatchInfo

