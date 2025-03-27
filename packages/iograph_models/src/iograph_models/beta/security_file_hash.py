from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFileHash(BaseModel):
	algorithm: Optional[SecurityFileHashAlgorithm | str] = Field(alias="algorithm", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_file_hash_algorithm import SecurityFileHashAlgorithm

