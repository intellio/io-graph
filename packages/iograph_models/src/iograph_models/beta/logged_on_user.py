from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LoggedOnUser(BaseModel):
	lastLogOnDateTime: Optional[datetime] = Field(alias="lastLogOnDateTime",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


