from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IosWebContentFilterAutoFilter(BaseModel):
	odata_type: Literal["#microsoft.graph.iosWebContentFilterAutoFilter"] = Field(alias="@odata.type", default="#microsoft.graph.iosWebContentFilterAutoFilter")
	allowedUrls: Optional[list[str]] = Field(alias="allowedUrls", default=None,)
	blockedUrls: Optional[list[str]] = Field(alias="blockedUrls", default=None,)

