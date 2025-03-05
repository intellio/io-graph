from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TemporaryAccessPassAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	isUsable: Optional[bool] = Field(alias="isUsable",default=None,)
	isUsableOnce: Optional[bool] = Field(alias="isUsableOnce",default=None,)
	lifetimeInMinutes: Optional[int] = Field(alias="lifetimeInMinutes",default=None,)
	methodUsabilityReason: Optional[str] = Field(alias="methodUsabilityReason",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	temporaryAccessPass: Optional[str] = Field(alias="temporaryAccessPass",default=None,)


