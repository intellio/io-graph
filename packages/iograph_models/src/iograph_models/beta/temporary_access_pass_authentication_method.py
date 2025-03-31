from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TemporaryAccessPassAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.temporaryAccessPassAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.temporaryAccessPassAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isUsableOnce: Optional[bool] = Field(alias="isUsableOnce", default=None,)
	lifetimeInMinutes: Optional[int] = Field(alias="lifetimeInMinutes", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	temporaryAccessPass: Optional[str] = Field(alias="temporaryAccessPass", default=None,)

