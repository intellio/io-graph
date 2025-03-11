from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SensitiveContentEvidence(BaseModel):
	length: Optional[int] = Field(alias="length",default=None,)
	match: Optional[str] = Field(alias="match",default=None,)
	offset: Optional[int] = Field(alias="offset",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


