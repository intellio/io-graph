from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_office365_active_user_detail_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Office365ActiveUserDetail]] = Field(alias="value", default=None,)

from .office365_active_user_detail import Office365ActiveUserDetail
