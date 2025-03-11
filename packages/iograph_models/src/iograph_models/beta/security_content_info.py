from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityContentInfo(BaseModel):
	contentFormat: Optional[str] = Field(alias="contentFormat",default=None,)
	identifier: Optional[str] = Field(alias="identifier",default=None,)
	metadata: Optional[list[SecurityKeyValuePair]] = Field(alias="metadata",default=None,)
	state: Optional[SecurityContentState | str] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_key_value_pair import SecurityKeyValuePair
from .security_content_state import SecurityContentState

