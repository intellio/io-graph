from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class KeyIntegerValuePair(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)
	odata_type: Literal["#microsoft.graph.keyIntegerValuePair"] = Field(alias="@odata.type", default="#microsoft.graph.keyIntegerValuePair")
	value: Optional[int] = Field(alias="value", default=None,)

