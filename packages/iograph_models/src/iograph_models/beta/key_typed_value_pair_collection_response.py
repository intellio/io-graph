from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class KeyTypedValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[KeyTypedValuePair]]] = Field(alias="value",default=None,)

from .key_typed_value_pair import KeyTypedValuePair

