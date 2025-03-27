from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFormattedContent(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	format: Optional[SecurityContentFormat | str] = Field(alias="format", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_content_format import SecurityContentFormat

