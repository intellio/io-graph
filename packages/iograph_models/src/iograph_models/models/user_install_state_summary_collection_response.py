from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserInstallStateSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserInstallStateSummary] = Field(alias="value",)

from .user_install_state_summary import UserInstallStateSummary

