from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_user_ids_with_flagged_app_registrationGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[str]] = Field(default=None,alias="value",)


