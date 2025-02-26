from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookOperationError(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	innerError: Optional[WorkbookOperationError] = Field(default=None,alias="innerError",)
	message: Optional[str] = Field(default=None,alias="message",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


