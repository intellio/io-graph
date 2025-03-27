from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Week_numPostRequest(BaseModel):
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	returnType: Optional[str] = Field(alias="returnType", default=None,)


