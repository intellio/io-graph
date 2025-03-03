from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Associate_with_hub_sitesPostRequest(BaseModel):
	hubSiteUrls: Optional[list[str]] = Field(default=None,alias="hubSiteUrls",)
	propagateToExistingLists: Optional[bool] = Field(default=None,alias="propagateToExistingLists",)


