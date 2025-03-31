from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventPresenterDetails(BaseModel):
	bio: Optional[ItemBody] = Field(alias="bio", default=None,)
	company: Optional[str] = Field(alias="company", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	linkedInProfileWebUrl: Optional[str] = Field(alias="linkedInProfileWebUrl", default=None,)
	personalSiteWebUrl: Optional[str] = Field(alias="personalSiteWebUrl", default=None,)
	photo: Optional[str] = Field(alias="photo", default=None,)
	twitterProfileWebUrl: Optional[str] = Field(alias="twitterProfileWebUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .item_body import ItemBody
