from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SimulationNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(default=None,alias="defaultLanguage",)
	endUserNotification: Optional[EndUserNotification] = Field(default=None,alias="endUserNotification",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	targettedUserType: Optional[TargettedUserType] = Field(default=None,alias="targettedUserType",)

from .end_user_notification import EndUserNotification
from .targetted_user_type import TargettedUserType

