from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MetaDataKeyStringPairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MetaDataKeyStringPair] = Field(alias="value",)

from .meta_data_key_string_pair import MetaDataKeyStringPair

