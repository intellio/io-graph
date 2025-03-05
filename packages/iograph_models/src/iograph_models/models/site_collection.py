from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SiteCollection(BaseModel):
	archivalDetails: Optional[SiteArchivalDetails] = Field(default=None,alias="archivalDetails",)
	dataLocationCode: Optional[str] = Field(default=None,alias="dataLocationCode",)
	hostname: Optional[str] = Field(default=None,alias="hostname",)
	root: Optional[Root] = Field(default=None,alias="root",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .site_archival_details import SiteArchivalDetails
from .root import Root

