from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrivilegedRoleSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedRoleSummary"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedRoleSummary")
	elevatedCount: Optional[int] = Field(alias="elevatedCount", default=None,)
	managedCount: Optional[int] = Field(alias="managedCount", default=None,)
	mfaEnabled: Optional[bool] = Field(alias="mfaEnabled", default=None,)
	status: Optional[RoleSummaryStatus | str] = Field(alias="status", default=None,)
	usersCount: Optional[int] = Field(alias="usersCount", default=None,)

from .role_summary_status import RoleSummaryStatus
