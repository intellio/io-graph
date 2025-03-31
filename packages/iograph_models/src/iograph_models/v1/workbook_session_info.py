from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookSessionInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	persistChanges: Optional[bool] = Field(alias="persistChanges", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

