from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IosWebContentFilterSpecificWebsitesAccess(BaseModel):
	odata_type: Literal["#microsoft.graph.iosWebContentFilterSpecificWebsitesAccess"] = Field(alias="@odata.type", default="#microsoft.graph.iosWebContentFilterSpecificWebsitesAccess")
	specificWebsitesOnly: Optional[list[IosBookmark]] = Field(alias="specificWebsitesOnly", default=None,)
	websiteList: Optional[list[IosBookmark]] = Field(alias="websiteList", default=None,)

from .ios_bookmark import IosBookmark
