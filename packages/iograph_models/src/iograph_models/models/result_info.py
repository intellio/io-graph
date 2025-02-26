from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResultInfo(BaseModel):
	code: Optional[int] = Field(default=None,alias="code",)
	message: Optional[str] = Field(default=None,alias="message",)
	subcode: Optional[int] = Field(default=None,alias="subcode",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


