from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_tokenPostRequest(BaseModel):
	tokenValidityInSeconds: Optional[int] = Field(alias="tokenValidityInSeconds", default=None,)


