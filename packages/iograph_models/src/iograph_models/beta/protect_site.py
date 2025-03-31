from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProtectSite(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.protectSite"] = Field(alias="@odata.type", default="#microsoft.graph.protectSite")
	accessType: Optional[SiteAccessType | str] = Field(alias="accessType", default=None,)
	conditionalAccessProtectionLevelId: Optional[str] = Field(alias="conditionalAccessProtectionLevelId", default=None,)

from .site_access_type import SiteAccessType
