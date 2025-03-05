from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_member_objectsPostRequest(BaseModel):
	securityEnabledOnly: Optional[bool] = Field(alias="securityEnabledOnly",default=None,)


