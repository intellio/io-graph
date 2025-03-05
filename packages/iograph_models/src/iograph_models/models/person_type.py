from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersonType(BaseModel):
	class_: Optional[str] = Field(default=None,alias="class",)
	subclass: Optional[str] = Field(default=None,alias="subclass",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


