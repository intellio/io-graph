from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventPresenterDetails(BaseModel):
	bio: Optional[ItemBody] = Field(default=None,alias="bio",)
	company: Optional[str] = Field(default=None,alias="company",)
	jobTitle: Optional[str] = Field(default=None,alias="jobTitle",)
	linkedInProfileWebUrl: Optional[str] = Field(default=None,alias="linkedInProfileWebUrl",)
	personalSiteWebUrl: Optional[str] = Field(default=None,alias="personalSiteWebUrl",)
	photo: Optional[str] = Field(default=None,alias="photo",)
	twitterProfileWebUrl: Optional[str] = Field(default=None,alias="twitterProfileWebUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .item_body import ItemBody

