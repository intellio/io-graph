from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LocalizedNotificationMessage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	messageTemplate: Optional[str] = Field(default=None,alias="messageTemplate",)
	subject: Optional[str] = Field(default=None,alias="subject",)


