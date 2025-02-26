from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FreeBusyError(BaseModel):
	message: Optional[str] = Field(default=None,alias="message",)
	responseCode: Optional[str] = Field(default=None,alias="responseCode",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


