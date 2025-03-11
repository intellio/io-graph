from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_recent_notebooks_with_includepersonalnotebooksGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[RecentNotebook]] = Field(alias="value",default=None,)

from .recent_notebook import RecentNotebook

