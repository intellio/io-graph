from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeleteAction(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	objectType: Optional[str] = Field(alias="objectType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


