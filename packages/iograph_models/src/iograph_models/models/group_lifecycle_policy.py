from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupLifecyclePolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	alternateNotificationEmails: Optional[str] = Field(default=None,alias="alternateNotificationEmails",)
	groupLifetimeInDays: Optional[int] = Field(default=None,alias="groupLifetimeInDays",)
	managedGroupTypes: Optional[str] = Field(default=None,alias="managedGroupTypes",)


