from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContentInfo(BaseModel):
	format: Optional[ContentFormat | str] = Field(alias="format", default=None,)
	identifier: Optional[str] = Field(alias="identifier", default=None,)
	metadata: Optional[list[KeyValuePair]] = Field(alias="metadata", default=None,)
	state: Optional[ContentState | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .content_format import ContentFormat
from .key_value_pair import KeyValuePair
from .content_state import ContentState

