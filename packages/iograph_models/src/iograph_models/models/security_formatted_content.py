from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFormattedContent(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	format: Optional[SecurityContentFormat] = Field(default=None,alias="format",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_content_format import SecurityContentFormat

