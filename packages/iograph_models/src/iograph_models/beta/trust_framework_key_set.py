from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TrustFrameworkKeySet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.trustFrameworkKeySet"] = Field(alias="@odata.type", default="#microsoft.graph.trustFrameworkKeySet")
	keys: Optional[list[TrustFrameworkKey]] = Field(alias="keys", default=None,)
	keys_v2: Optional[list[TrustFrameworkKey_v2]] = Field(alias="keys_v2", default=None,)

from .trust_framework_key import TrustFrameworkKey
from .trust_framework_key_v2 import TrustFrameworkKey_v2
