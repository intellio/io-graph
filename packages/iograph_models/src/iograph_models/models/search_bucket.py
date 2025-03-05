from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchBucket(BaseModel):
	aggregationFilterToken: Optional[str] = Field(default=None,alias="aggregationFilterToken",)
	count: Optional[int] = Field(default=None,alias="count",)
	key: Optional[str] = Field(default=None,alias="key",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


