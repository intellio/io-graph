from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventPresenter(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	identity: SerializeAsAny[Optional[Identity]] = Field(alias="identity",default=None,)
	presenterDetails: Optional[VirtualEventPresenterDetails] = Field(alias="presenterDetails",default=None,)
	sessions: Optional[list[VirtualEventSession]] = Field(alias="sessions",default=None,)

from .identity import Identity
from .virtual_event_presenter_details import VirtualEventPresenterDetails
from .virtual_event_session import VirtualEventSession

