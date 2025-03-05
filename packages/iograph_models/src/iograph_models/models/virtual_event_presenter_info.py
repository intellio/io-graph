from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventPresenterInfo(BaseModel):
	identity: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="identity",)
	role: Optional[OnlineMeetingRole] = Field(default=None,alias="role",)
	upn: Optional[str] = Field(default=None,alias="upn",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	presenterDetails: Optional[VirtualEventPresenterDetails] = Field(default=None,alias="presenterDetails",)

from .identity_set import IdentitySet
from .online_meeting_role import OnlineMeetingRole
from .virtual_event_presenter_details import VirtualEventPresenterDetails

