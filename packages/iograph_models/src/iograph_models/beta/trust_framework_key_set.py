from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrustFrameworkKeySet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	keys: Optional[list[TrustFrameworkKey]] = Field(alias="keys", default=None,)
	keys_v2: Optional[list[TrustFrameworkKey_v2]] = Field(alias="keys_v2", default=None,)

from .trust_framework_key import TrustFrameworkKey
from .trust_framework_key_v2 import TrustFrameworkKey_v2

