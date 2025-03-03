from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PublicInnerError(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	details: Optional[list[PublicErrorDetail]] = Field(default=None,alias="details",)
	message: Optional[str] = Field(default=None,alias="message",)
	target: Optional[str] = Field(default=None,alias="target",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .public_error_detail import PublicErrorDetail

