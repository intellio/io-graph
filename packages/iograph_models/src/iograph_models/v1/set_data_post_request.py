from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_dataPostRequest(BaseModel):
	sourceData: Optional[str] = Field(alias="sourceData",default=None,)
	seriesBy: Optional[str] = Field(alias="seriesBy",default=None,)


