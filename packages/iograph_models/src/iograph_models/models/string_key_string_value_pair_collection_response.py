from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StringKeyStringValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[StringKeyStringValuePair]] = Field(default=None,alias="value",)

from .string_key_string_value_pair import StringKeyStringValuePair

