from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TextWebPart(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.textWebPart"] = Field(alias="@odata.type", default="#microsoft.graph.textWebPart")
	innerHtml: Optional[str] = Field(alias="innerHtml", default=None,)

