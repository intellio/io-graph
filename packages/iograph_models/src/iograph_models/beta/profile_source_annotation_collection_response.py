from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProfileSourceAnnotationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ProfileSourceAnnotation]] = Field(alias="value", default=None,)

from .profile_source_annotation import ProfileSourceAnnotation
