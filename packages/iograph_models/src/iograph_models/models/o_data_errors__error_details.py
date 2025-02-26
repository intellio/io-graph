from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ODataErrorsErrorDetails(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	message: Optional[str] = Field(default=None,alias="message",)
	target: Optional[str] = Field(default=None,alias="target",)


