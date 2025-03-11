from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Dimension(BaseModel):
	code: Optional[str] = Field(alias="code",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	dimensionValues: Optional[list[DimensionValue]] = Field(alias="dimensionValues",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .dimension_value import DimensionValue

