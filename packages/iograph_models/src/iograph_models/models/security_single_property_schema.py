from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySinglePropertySchema(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


