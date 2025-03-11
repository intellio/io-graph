from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeNotificationCollection(BaseModel):
	validationTokens: Optional[list[str]] = Field(alias="validationTokens",default=None,)
	value: Optional[list[ChangeNotification]] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .change_notification import ChangeNotification

