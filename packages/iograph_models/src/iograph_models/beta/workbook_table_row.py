from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookTableRow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	index: Optional[int] = Field(alias="index", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)


