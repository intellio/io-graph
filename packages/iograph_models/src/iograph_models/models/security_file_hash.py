from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFileHash(BaseModel):
	algorithm: Optional[SecurityFileHashAlgorithm] = Field(default=None,alias="algorithm",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_file_hash_algorithm import SecurityFileHashAlgorithm

