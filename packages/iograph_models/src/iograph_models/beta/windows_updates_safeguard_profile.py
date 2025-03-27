from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesSafeguardProfile(BaseModel):
	category: Optional[WindowsUpdatesSafeguardCategory | str] = Field(alias="category", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_safeguard_category import WindowsUpdatesSafeguardCategory

