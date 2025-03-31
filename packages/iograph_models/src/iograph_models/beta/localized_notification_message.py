from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class LocalizedNotificationMessage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.localizedNotificationMessage"] = Field(alias="@odata.type",)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	messageTemplate: Optional[str] = Field(alias="messageTemplate", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)

