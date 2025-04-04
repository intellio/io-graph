from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MultiValueLegacyExtendedProperty(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.multiValueLegacyExtendedProperty"] = Field(alias="@odata.type", default="#microsoft.graph.multiValueLegacyExtendedProperty")
	value: Optional[list[str]] = Field(alias="value", default=None,)

