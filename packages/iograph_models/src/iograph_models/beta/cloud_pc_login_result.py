from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcLoginResult(BaseModel):
	time: Optional[datetime] = Field(alias="time",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


