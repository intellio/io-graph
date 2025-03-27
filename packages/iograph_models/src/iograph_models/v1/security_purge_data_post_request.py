from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_purge_dataPostRequest(BaseModel):
	purgeType: Optional[SecurityPurgeType | str] = Field(alias="purgeType", default=None,)
	purgeAreas: Optional[SecurityPurgeAreas | str] = Field(alias="purgeAreas", default=None,)

from .security_purge_type import SecurityPurgeType
from .security_purge_areas import SecurityPurgeAreas

