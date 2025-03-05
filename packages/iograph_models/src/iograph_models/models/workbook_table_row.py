from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookTableRow(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	index: Optional[int] = Field(default=None,alias="index",)
	values: Optional[str] = Field(default=None,alias="values",)


