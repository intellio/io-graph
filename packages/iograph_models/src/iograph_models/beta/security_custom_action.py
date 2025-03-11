from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCustomAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	properties: Optional[list[SecurityKeyValuePair]] = Field(alias="properties",default=None,)

from .security_key_value_pair import SecurityKeyValuePair

