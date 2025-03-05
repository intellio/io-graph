from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InternetExplorerMode(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	siteLists: Optional[list[BrowserSiteList]] = Field(default=None,alias="siteLists",)

from .browser_site_list import BrowserSiteList

