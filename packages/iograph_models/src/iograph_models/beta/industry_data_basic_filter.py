from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataBasicFilter(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attribute: Optional[IndustryDataFilterOptions | str] = Field(alias="attribute",default=None,)
	in_: Optional[list[str]] = Field(alias="in",default=None,)

from .industry_data_filter_options import IndustryDataFilterOptions

