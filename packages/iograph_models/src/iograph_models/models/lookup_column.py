from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LookupColumn(BaseModel):
	allowMultipleValues: Optional[bool] = Field(default=None,alias="allowMultipleValues",)
	allowUnlimitedLength: Optional[bool] = Field(default=None,alias="allowUnlimitedLength",)
	columnName: Optional[str] = Field(default=None,alias="columnName",)
	listId: Optional[str] = Field(default=None,alias="listId",)
	primaryLookupColumnId: Optional[str] = Field(default=None,alias="primaryLookupColumnId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


