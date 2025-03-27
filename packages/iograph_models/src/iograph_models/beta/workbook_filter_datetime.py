from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFilterDatetime(BaseModel):
	date: Optional[str] = Field(alias="date", default=None,)
	specificity: Optional[str] = Field(alias="specificity", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


