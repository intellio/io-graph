from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppReturnCode(BaseModel):
	returnCode: Optional[int] = Field(alias="returnCode", default=None,)
	type: Optional[Win32LobAppReturnCodeType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .win32_lob_app_return_code_type import Win32LobAppReturnCodeType

