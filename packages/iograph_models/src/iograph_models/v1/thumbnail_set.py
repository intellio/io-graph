from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ThumbnailSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.thumbnailSet"] = Field(alias="@odata.type",)
	large: Optional[Thumbnail] = Field(alias="large", default=None,)
	medium: Optional[Thumbnail] = Field(alias="medium", default=None,)
	small: Optional[Thumbnail] = Field(alias="small", default=None,)
	source: Optional[Thumbnail] = Field(alias="source", default=None,)

from .thumbnail import Thumbnail
