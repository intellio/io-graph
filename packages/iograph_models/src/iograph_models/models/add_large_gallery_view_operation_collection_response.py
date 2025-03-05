from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddLargeGalleryViewOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AddLargeGalleryViewOperation]] = Field(default=None,alias="value",)

from .add_large_gallery_view_operation import AddLargeGalleryViewOperation

