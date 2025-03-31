from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SiteArchivalDetails(BaseModel):
	archiveStatus: Optional[SiteArchiveStatus | str] = Field(alias="archiveStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .site_archive_status import SiteArchiveStatus
