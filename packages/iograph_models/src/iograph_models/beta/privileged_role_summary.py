from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedRoleSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	elevatedCount: Optional[int] = Field(alias="elevatedCount", default=None,)
	managedCount: Optional[int] = Field(alias="managedCount", default=None,)
	mfaEnabled: Optional[bool] = Field(alias="mfaEnabled", default=None,)
	status: Optional[RoleSummaryStatus | str] = Field(alias="status", default=None,)
	usersCount: Optional[int] = Field(alias="usersCount", default=None,)

from .role_summary_status import RoleSummaryStatus

