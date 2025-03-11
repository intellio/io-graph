from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ThumbnailSet(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	large: Optional[Thumbnail] = Field(alias="large",default=None,)
	medium: Optional[Thumbnail] = Field(alias="medium",default=None,)
	small: Optional[Thumbnail] = Field(alias="small",default=None,)
	source: Optional[Thumbnail] = Field(alias="source",default=None,)

from .thumbnail import Thumbnail
from .thumbnail import Thumbnail
from .thumbnail import Thumbnail
from .thumbnail import Thumbnail

