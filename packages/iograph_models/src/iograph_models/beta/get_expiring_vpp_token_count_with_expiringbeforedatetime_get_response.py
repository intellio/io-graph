from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_expiring_vpp_token_count_with_expiringbeforedatetimeGetResponse(BaseModel):
	value: Optional[int] = Field(alias="value",default=None,)


