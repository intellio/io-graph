from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SimulationNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage", default=None,)
	endUserNotification: Optional[EndUserNotification] = Field(alias="endUserNotification", default=None,)
	odata_type: Literal["#microsoft.graph.simulationNotification"] = Field(alias="@odata.type", default="#microsoft.graph.simulationNotification")
	targettedUserType: Optional[TargettedUserType | str] = Field(alias="targettedUserType", default=None,)

from .end_user_notification import EndUserNotification
from .targetted_user_type import TargettedUserType

