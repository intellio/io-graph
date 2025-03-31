from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AttributeSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.attributeSet"] = Field(alias="@odata.type",)
	description: Optional[str] = Field(alias="description", default=None,)
	maxAttributesPerSet: Optional[int] = Field(alias="maxAttributesPerSet", default=None,)

