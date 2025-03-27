from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataBasicFilter(BaseModel):
	odata_type: Literal["#microsoft.graph.industryData.basicFilter"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.basicFilter")
	attribute: Optional[IndustryDataFilterOptions | str] = Field(alias="attribute", default=None,)
	in_: Optional[list[str]] = Field(alias="in", default=None,)

from .industry_data_filter_options import IndustryDataFilterOptions

