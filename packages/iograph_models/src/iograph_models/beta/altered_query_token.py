from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AlteredQueryToken(BaseModel):
	length: Optional[int] = Field(alias="length",default=None,)
	offset: Optional[int] = Field(alias="offset",default=None,)
	suggestion: Optional[str] = Field(alias="suggestion",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


