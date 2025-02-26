from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InternetExplorerMode(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	siteLists: list[BrowserSiteList] = Field(alias="siteLists",)

from .browser_site_list import BrowserSiteList

