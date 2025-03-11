from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Associate_with_hub_sitesPostRequest(BaseModel):
	hubSiteUrls: Optional[list[str]] = Field(alias="hubSiteUrls",default=None,)
	propagateToExistingLists: Optional[bool] = Field(alias="propagateToExistingLists",default=None,)


