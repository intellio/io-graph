from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityCasesRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	ediscoveryCases: list[SecurityEdiscoveryCase] = Field(alias="ediscoveryCases",)

from .security_ediscovery_case import SecurityEdiscoveryCase

