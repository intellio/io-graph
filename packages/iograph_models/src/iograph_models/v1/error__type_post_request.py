from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Error__typePostRequest(BaseModel):
	errorVal: Optional[str] = Field(alias="errorVal", default=None,)


