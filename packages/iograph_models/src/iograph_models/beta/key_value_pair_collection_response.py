from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class KeyValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[KeyValuePair]] = Field(alias="value",default=None,)

from .key_value_pair import KeyValuePair

