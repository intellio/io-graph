from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFunctionResult(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	error: Optional[str] = Field(default=None,alias="error",)
	value: Optional[str] = Field(default=None,alias="value",)


