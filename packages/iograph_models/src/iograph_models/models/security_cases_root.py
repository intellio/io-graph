from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCasesRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	ediscoveryCases: Optional[list[SecurityEdiscoveryCase]] = Field(default=None,alias="ediscoveryCases",)

from .security_ediscovery_case import SecurityEdiscoveryCase

