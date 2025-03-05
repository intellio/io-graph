from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFilterDatetime(BaseModel):
	date: Optional[str] = Field(default=None,alias="date",)
	specificity: Optional[str] = Field(default=None,alias="specificity",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


