from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StringKeyStringValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[StringKeyStringValuePair]] = Field(alias="value",default=None,)

from .string_key_string_value_pair import StringKeyStringValuePair

