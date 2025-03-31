from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataIndustryDataRunCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IndustryDataIndustryDataRun]] = Field(alias="value", default=None,)

from .industry_data_industry_data_run import IndustryDataIndustryDataRun
