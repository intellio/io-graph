from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PersistentBrowserSessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.persistentBrowserSessionControl"] = Field(alias="@odata.type", default="#microsoft.graph.persistentBrowserSessionControl")
	mode: Optional[PersistentBrowserSessionMode | str] = Field(alias="mode", default=None,)

from .persistent_browser_session_mode import PersistentBrowserSessionMode
