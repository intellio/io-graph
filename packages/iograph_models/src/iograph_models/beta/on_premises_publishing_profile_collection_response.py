from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesPublishingProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OnPremisesPublishingProfile]] = Field(alias="value", default=None,)

from .on_premises_publishing_profile import OnPremisesPublishingProfile
