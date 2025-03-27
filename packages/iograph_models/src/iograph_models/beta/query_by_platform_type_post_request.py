from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Query_by_platform_typePostRequest(BaseModel):
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)

from .policy_platform_type import PolicyPlatformType

