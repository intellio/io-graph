from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage",default=None,)
	endUserNotification: Optional[EndUserNotification] = Field(alias="endUserNotification",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	targettedUserType: Optional[TargettedUserType | str] = Field(alias="targettedUserType",default=None,)

from .end_user_notification import EndUserNotification
from .targetted_user_type import TargettedUserType

