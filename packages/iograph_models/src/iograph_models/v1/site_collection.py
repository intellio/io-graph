from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SiteCollection(BaseModel):
	archivalDetails: Optional[SiteArchivalDetails] = Field(alias="archivalDetails", default=None,)
	dataLocationCode: Optional[str] = Field(alias="dataLocationCode", default=None,)
	hostname: Optional[str] = Field(alias="hostname", default=None,)
	root: Optional[Root] = Field(alias="root", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .site_archival_details import SiteArchivalDetails
from .root import Root
