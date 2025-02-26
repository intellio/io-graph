from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_purge_dataPostRequest(BaseModel):
	purgeType: Optional[SecurityPurgeType] = Field(default=None,alias="purgeType",)
	purgeAreas: Optional[SecurityPurgeAreas] = Field(default=None,alias="purgeAreas",)

from .security_purge_type import SecurityPurgeType
from .security_purge_areas import SecurityPurgeAreas

