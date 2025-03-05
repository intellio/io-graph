from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StringKeyObjectValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[StringKeyObjectValuePair]] = Field(default=None,alias="value",)

from .string_key_object_value_pair import StringKeyObjectValuePair

