from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExactDataMatchStoreColumnCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ExactDataMatchStoreColumn]] = Field(alias="value", default=None,)

from .exact_data_match_store_column import ExactDataMatchStoreColumn

