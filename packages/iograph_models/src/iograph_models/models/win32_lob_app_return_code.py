from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppReturnCode(BaseModel):
	returnCode: Optional[int] = Field(default=None,alias="returnCode",)
	type: Optional[Win32LobAppReturnCodeType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .win32_lob_app_return_code_type import Win32LobAppReturnCodeType

