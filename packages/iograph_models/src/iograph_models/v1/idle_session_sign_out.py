from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdleSessionSignOut(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	signOutAfterInSeconds: Optional[int] = Field(alias="signOutAfterInSeconds",default=None,)
	warnAfterInSeconds: Optional[int] = Field(alias="warnAfterInSeconds",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


