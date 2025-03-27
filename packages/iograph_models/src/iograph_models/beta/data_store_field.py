from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DataStoreField(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	searchable: Optional[bool] = Field(alias="searchable", default=None,)
	unique: Optional[bool] = Field(alias="unique", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


