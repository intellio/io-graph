from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class KeyBooleanValuePair(BaseModel):
	key: Optional[str] = Field(alias="key",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	value: Optional[bool] = Field(alias="value",default=None,)


