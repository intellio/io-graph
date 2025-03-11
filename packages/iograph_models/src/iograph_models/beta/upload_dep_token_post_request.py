from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Upload_dep_tokenPostRequest(BaseModel):
	appleId: Optional[str] = Field(alias="appleId",default=None,)
	depToken: Optional[str] = Field(alias="depToken",default=None,)


