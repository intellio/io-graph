from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrainingCampaignCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TrainingCampaign]] = Field(alias="value", default=None,)

from .training_campaign import TrainingCampaign
