from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows_updates_unenroll_assets_by_idPostRequest(BaseModel):
	updateCategory: Optional[WindowsUpdatesUpdateCategory | str] = Field(alias="updateCategory", default=None,)
	memberEntityType: Optional[str] = Field(alias="memberEntityType", default=None,)
	ids: Optional[list[str]] = Field(alias="ids", default=None,)

from .windows_updates_update_category import WindowsUpdatesUpdateCategory
