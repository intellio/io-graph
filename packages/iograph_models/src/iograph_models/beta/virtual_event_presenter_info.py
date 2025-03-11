from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventPresenterInfo(BaseModel):
	identity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="identity",default=None,)
	role: Optional[OnlineMeetingRole | str] = Field(alias="role",default=None,)
	upn: Optional[str] = Field(alias="upn",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	presenterDetails: Optional[VirtualEventPresenterDetails] = Field(alias="presenterDetails",default=None,)

from .identity_set import IdentitySet
from .online_meeting_role import OnlineMeetingRole
from .virtual_event_presenter_details import VirtualEventPresenterDetails

