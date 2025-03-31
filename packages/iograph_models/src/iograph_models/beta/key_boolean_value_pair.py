from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class KeyBooleanValuePair(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)
	odata_type: Literal["#microsoft.graph.keyBooleanValuePair"] = Field(alias="@odata.type", default="#microsoft.graph.keyBooleanValuePair")
	value: Optional[bool] = Field(alias="value", default=None,)

