from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddLargeGalleryViewOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AddLargeGalleryViewOperation]] = Field(alias="value",default=None,)

from .add_large_gallery_view_operation import AddLargeGalleryViewOperation

