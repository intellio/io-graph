from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Folder(BaseModel):
	childCount: Optional[int] = Field(alias="childCount",default=None,)
	view: Optional[FolderView] = Field(alias="view",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .folder_view import FolderView

