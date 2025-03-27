from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DateTimeColumn(BaseModel):
	displayAs: Optional[str] = Field(alias="displayAs", default=None,)
	format: Optional[str] = Field(alias="format", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


