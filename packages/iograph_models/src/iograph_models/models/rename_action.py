from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RenameAction(BaseModel):
	newName: Optional[str] = Field(default=None,alias="newName",)
	oldName: Optional[str] = Field(default=None,alias="oldName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


