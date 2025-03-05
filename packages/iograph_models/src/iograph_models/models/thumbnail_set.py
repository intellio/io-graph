from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ThumbnailSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	large: Optional[Thumbnail] = Field(default=None,alias="large",)
	medium: Optional[Thumbnail] = Field(default=None,alias="medium",)
	small: Optional[Thumbnail] = Field(default=None,alias="small",)
	source: Optional[Thumbnail] = Field(default=None,alias="source",)

from .thumbnail import Thumbnail
from .thumbnail import Thumbnail
from .thumbnail import Thumbnail
from .thumbnail import Thumbnail

