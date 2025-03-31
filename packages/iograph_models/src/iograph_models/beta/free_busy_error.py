from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FreeBusyError(BaseModel):
	message: Optional[str] = Field(alias="message", default=None,)
	responseCode: Optional[str] = Field(alias="responseCode", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

