from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TabUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="initiator",)
	tabId: Optional[str] = Field(default=None,alias="tabId",)

from .identity_set import IdentitySet

