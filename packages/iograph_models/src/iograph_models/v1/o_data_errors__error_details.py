from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ODataErrorsErrorDetails(BaseModel):
	code: Optional[str] = Field(alias="code",default=None,)
	message: Optional[str] = Field(alias="message",default=None,)
	target: Optional[str] = Field(alias="target",default=None,)


