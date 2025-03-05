from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersistentBrowserSessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	mode: Optional[PersistentBrowserSessionMode | str] = Field(alias="mode",default=None,)

from .persistent_browser_session_mode import PersistentBrowserSessionMode

