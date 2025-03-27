from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClassificationAttribute(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	count: Optional[int] = Field(alias="count", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


