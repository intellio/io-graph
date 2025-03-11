from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectSite(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessType: Optional[SiteAccessType | str] = Field(alias="accessType",default=None,)
	conditionalAccessProtectionLevelId: Optional[str] = Field(alias="conditionalAccessProtectionLevelId",default=None,)

from .site_access_type import SiteAccessType

