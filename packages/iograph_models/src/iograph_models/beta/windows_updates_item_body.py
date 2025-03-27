from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesItemBody(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	contentType: Optional[WindowsUpdatesBodyType | str] = Field(alias="contentType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_body_type import WindowsUpdatesBodyType

