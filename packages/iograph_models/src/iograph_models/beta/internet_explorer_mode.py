from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InternetExplorerMode(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	siteLists: Optional[list[BrowserSiteList]] = Field(alias="siteLists", default=None,)

from .browser_site_list import BrowserSiteList

