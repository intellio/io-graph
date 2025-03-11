from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserGovernanceCriteria(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)


