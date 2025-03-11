from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosWebContentFilterSpecificWebsitesAccess(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	specificWebsitesOnly: Optional[list[IosBookmark]] = Field(alias="specificWebsitesOnly",default=None,)
	websiteList: Optional[list[IosBookmark]] = Field(alias="websiteList",default=None,)

from .ios_bookmark import IosBookmark
from .ios_bookmark import IosBookmark

