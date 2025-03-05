from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AlteredQueryToken(BaseModel):
	length: Optional[int] = Field(default=None,alias="length",)
	offset: Optional[int] = Field(default=None,alias="offset",)
	suggestion: Optional[str] = Field(default=None,alias="suggestion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


