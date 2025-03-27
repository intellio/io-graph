from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Record_decisionsPostRequest(BaseModel):
	reviewResult: Optional[str] = Field(alias="reviewResult", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)


