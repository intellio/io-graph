from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OperationError(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	message: Optional[str] = Field(default=None,alias="message",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


