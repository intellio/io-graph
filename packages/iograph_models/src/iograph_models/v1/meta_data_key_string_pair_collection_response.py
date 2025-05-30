from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MetaDataKeyStringPairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MetaDataKeyStringPair]] = Field(alias="value", default=None,)

from .meta_data_key_string_pair import MetaDataKeyStringPair
