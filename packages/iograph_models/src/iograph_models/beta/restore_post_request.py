from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePostRequest(BaseModel):
	newUserPrincipalName: Optional[str] = Field(alias="newUserPrincipalName", default=None,)


