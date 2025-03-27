from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCdpColdCrawlStatusRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpColdCrawlStatusRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpColdCrawlStatusRecord")


