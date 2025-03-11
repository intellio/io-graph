from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminWindows(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	updates: Optional[AdminWindowsUpdates] = Field(alias="updates",default=None,)

from .admin_windows_updates import AdminWindowsUpdates

