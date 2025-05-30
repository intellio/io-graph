from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Submit_ti_indicatorsPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TiIndicator]] = Field(alias="value", default=None,)

from .ti_indicator import TiIndicator
