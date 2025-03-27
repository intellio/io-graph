from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StringKeyObjectValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[StringKeyObjectValuePair]] = Field(alias="value", default=None,)

from .string_key_object_value_pair import StringKeyObjectValuePair

