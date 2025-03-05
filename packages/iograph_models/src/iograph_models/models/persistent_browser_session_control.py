from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersistentBrowserSessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	mode: Optional[PersistentBrowserSessionMode] = Field(default=None,alias="mode",)

from .persistent_browser_session_mode import PersistentBrowserSessionMode

