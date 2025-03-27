from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RenameAction(BaseModel):
	newName: Optional[str] = Field(alias="newName", default=None,)
	oldName: Optional[str] = Field(alias="oldName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


