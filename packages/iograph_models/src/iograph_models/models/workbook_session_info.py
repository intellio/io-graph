from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookSessionInfo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	persistChanges: Optional[bool] = Field(default=None,alias="persistChanges",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


