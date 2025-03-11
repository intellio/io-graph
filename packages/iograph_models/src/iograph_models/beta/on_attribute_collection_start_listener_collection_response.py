from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[OnAttributeCollectionStartListener]] = Field(alias="value",default=None,)

from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener

