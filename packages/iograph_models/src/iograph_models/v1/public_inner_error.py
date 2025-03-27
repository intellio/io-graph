from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PublicInnerError(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	details: Optional[list[PublicErrorDetail]] = Field(alias="details", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	target: Optional[str] = Field(alias="target", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .public_error_detail import PublicErrorDetail

