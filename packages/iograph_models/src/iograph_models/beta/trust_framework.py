from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrustFramework(BaseModel):
	keySets: Optional[list[TrustFrameworkKeySet]] = Field(alias="keySets", default=None,)
	policies: Optional[list[TrustFrameworkPolicy]] = Field(alias="policies", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .trust_framework_key_set import TrustFrameworkKeySet
from .trust_framework_policy import TrustFrameworkPolicy
