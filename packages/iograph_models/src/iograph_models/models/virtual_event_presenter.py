from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventPresenter(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	email: Optional[str] = Field(default=None,alias="email",)
	identity: Optional[Identity] = Field(default=None,alias="identity",)
	presenterDetails: Optional[VirtualEventPresenterDetails] = Field(default=None,alias="presenterDetails",)

from .identity import Identity
from .virtual_event_presenter_details import VirtualEventPresenterDetails

