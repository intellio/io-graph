from __future__ import annotations
from pydantic import BaseModel, Field


class Identity_governance_activatePostRequest(BaseModel):
	subjects: list[User] = Field(alias="subjects",)

from .user import User

