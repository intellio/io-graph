from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Folder(BaseModel):
	childCount: Optional[int] = Field(default=None,alias="childCount",)
	view: Optional[FolderView] = Field(default=None,alias="view",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .folder_view import FolderView

