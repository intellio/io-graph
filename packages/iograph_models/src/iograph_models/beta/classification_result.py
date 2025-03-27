from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClassificationResult(BaseModel):
	confidenceLevel: Optional[int] = Field(alias="confidenceLevel", default=None,)
	count: Optional[int] = Field(alias="count", default=None,)
	sensitiveTypeId: Optional[str] = Field(alias="sensitiveTypeId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


