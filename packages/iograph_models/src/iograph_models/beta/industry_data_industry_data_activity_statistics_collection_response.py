from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataActivityStatisticsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[IndustryDataIndustryDataActivityStatistics]]] = Field(alias="value",default=None,)

from .industry_data_industry_data_activity_statistics import IndustryDataIndustryDataActivityStatistics

