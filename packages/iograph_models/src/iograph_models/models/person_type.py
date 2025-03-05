from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersonType(BaseModel):
	class_: Optional[str] = Field(alias="class",default=None,)
	subclass: Optional[str] = Field(alias="subclass",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


