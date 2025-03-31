from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Complete_setupPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[RoleSuccessStatistics]] = Field(alias="value", default=None,)

from .role_success_statistics import RoleSuccessStatistics
