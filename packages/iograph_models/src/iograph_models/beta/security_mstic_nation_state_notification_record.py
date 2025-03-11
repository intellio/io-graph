from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMsticNationStateNotificationRecord(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


