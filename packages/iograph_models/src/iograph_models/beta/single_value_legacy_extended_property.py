from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SingleValueLegacyExtendedProperty(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.singleValueLegacyExtendedProperty"] = Field(alias="@odata.type", default="#microsoft.graph.singleValueLegacyExtendedProperty")
	value: Optional[str] = Field(alias="value", default=None,)

