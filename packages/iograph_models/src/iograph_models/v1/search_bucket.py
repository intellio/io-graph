from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchBucket(BaseModel):
	aggregationFilterToken: Optional[str] = Field(alias="aggregationFilterToken", default=None,)
	count: Optional[int] = Field(alias="count", default=None,)
	key: Optional[str] = Field(alias="key", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


