from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Identity_governance_activatePostRequest(BaseModel):
	subjects: Optional[list[User]] = Field(alias="subjects", default=None,)

from .user import User

