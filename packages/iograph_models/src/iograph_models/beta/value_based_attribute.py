from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ValueBasedAttribute(BaseModel):
	odata_type: Literal["#microsoft.graph.valueBasedAttribute"] = Field(alias="@odata.type", default="#microsoft.graph.valueBasedAttribute")
	value: Optional[str] = Field(alias="value", default=None,)


