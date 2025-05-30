from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Submit_ti_indicatorsPostRequest(BaseModel):
	value: Optional[list[TiIndicator]] = Field(alias="value", default=None,)

from .ti_indicator import TiIndicator
