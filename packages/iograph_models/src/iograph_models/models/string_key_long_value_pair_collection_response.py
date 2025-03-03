from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StringKeyLongValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[StringKeyLongValuePair]] = Field(default=None,alias="value",)

from .string_key_long_value_pair import StringKeyLongValuePair

