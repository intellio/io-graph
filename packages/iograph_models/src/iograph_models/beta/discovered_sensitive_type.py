from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DiscoveredSensitiveType(BaseModel):
	classificationAttributes: Optional[list[ClassificationAttribute]] = Field(alias="classificationAttributes",default=None,)
	confidence: Optional[int] = Field(alias="confidence",default=None,)
	count: Optional[int] = Field(alias="count",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .classification_attribute import ClassificationAttribute

