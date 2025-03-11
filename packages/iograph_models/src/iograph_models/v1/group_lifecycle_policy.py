from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupLifecyclePolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alternateNotificationEmails: Optional[str] = Field(alias="alternateNotificationEmails",default=None,)
	groupLifetimeInDays: Optional[int] = Field(alias="groupLifetimeInDays",default=None,)
	managedGroupTypes: Optional[str] = Field(alias="managedGroupTypes",default=None,)


