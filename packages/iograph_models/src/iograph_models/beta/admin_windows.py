from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminWindows(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminWindows"] = Field(alias="@odata.type",)
	updates: Optional[AdminWindowsUpdates] = Field(alias="updates", default=None,)

from .admin_windows_updates import AdminWindowsUpdates
