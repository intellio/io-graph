from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChoosePostRequest(BaseModel):
	indexNum: Optional[str] = Field(alias="indexNum",default=None,)
	values: Optional[str] = Field(alias="values",default=None,)


