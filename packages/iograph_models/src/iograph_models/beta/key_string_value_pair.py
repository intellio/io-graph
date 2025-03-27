from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class KeyStringValuePair(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)
	odata_type: Literal["#microsoft.graph.keyStringValuePair"] = Field(alias="@odata.type", default="#microsoft.graph.keyStringValuePair")
	value: Optional[str] = Field(alias="value", default=None,)


