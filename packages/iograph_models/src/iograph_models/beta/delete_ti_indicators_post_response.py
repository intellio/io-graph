from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Delete_ti_indicatorsPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ResultInfo]] = Field(alias="value", default=None,)

from .result_info import ResultInfo
