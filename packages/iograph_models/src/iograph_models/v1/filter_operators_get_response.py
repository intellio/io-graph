from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Filter_operatorsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[FilterOperatorSchema]] = Field(alias="value", default=None,)

from .filter_operator_schema import FilterOperatorSchema
