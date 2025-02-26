from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TemporaryAccessPassAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	isUsable: Optional[bool] = Field(default=None,alias="isUsable",)
	isUsableOnce: Optional[bool] = Field(default=None,alias="isUsableOnce",)
	lifetimeInMinutes: Optional[int] = Field(default=None,alias="lifetimeInMinutes",)
	methodUsabilityReason: Optional[str] = Field(default=None,alias="methodUsabilityReason",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	temporaryAccessPass: Optional[str] = Field(default=None,alias="temporaryAccessPass",)


