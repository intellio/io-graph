from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsItemIdResolver(BaseModel):
	priority: Optional[int] = Field(alias="priority",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	itemId: Optional[str] = Field(alias="itemId",default=None,)
	urlMatchInfo: Optional[ExternalConnectorsUrlMatchInfo] = Field(alias="urlMatchInfo",default=None,)

from .external_connectors_url_match_info import ExternalConnectorsUrlMatchInfo

