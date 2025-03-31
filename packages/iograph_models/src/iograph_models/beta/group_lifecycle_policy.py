from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GroupLifecyclePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupLifecyclePolicy"] = Field(alias="@odata.type",)
	alternateNotificationEmails: Optional[str] = Field(alias="alternateNotificationEmails", default=None,)
	groupLifetimeInDays: Optional[int] = Field(alias="groupLifetimeInDays", default=None,)
	managedGroupTypes: Optional[str] = Field(alias="managedGroupTypes", default=None,)

