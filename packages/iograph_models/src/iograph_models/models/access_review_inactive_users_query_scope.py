from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewInactiveUsersQueryScope(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	query: Optional[str] = Field(default=None,alias="query",)
	queryRoot: Optional[str] = Field(default=None,alias="queryRoot",)
	queryType: Optional[str] = Field(default=None,alias="queryType",)
	inactiveDuration: Optional[str] = Field(default=None,alias="inactiveDuration",)


