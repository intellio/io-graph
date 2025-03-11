from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubstitutePostRequest(BaseModel):
	text: Optional[str] = Field(alias="text",default=None,)
	oldText: Optional[str] = Field(alias="oldText",default=None,)
	newText: Optional[str] = Field(alias="newText",default=None,)
	instanceNum: Optional[str] = Field(alias="instanceNum",default=None,)


