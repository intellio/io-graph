from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Cancel_approvalPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)


