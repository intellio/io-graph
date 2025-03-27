from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DelegationSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	allowedActions: Optional[DelegateAllowedActions] = Field(alias="allowedActions", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)

from .delegate_allowed_actions import DelegateAllowedActions

