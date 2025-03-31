from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnAttributeCollectionStartCustomExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OnAttributeCollectionStartCustomExtension]] = Field(alias="value", default=None,)

from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
