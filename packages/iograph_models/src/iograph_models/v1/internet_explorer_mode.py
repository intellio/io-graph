from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InternetExplorerMode(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.internetExplorerMode"] = Field(alias="@odata.type",)
	siteLists: Optional[list[BrowserSiteList]] = Field(alias="siteLists", default=None,)

from .browser_site_list import BrowserSiteList
