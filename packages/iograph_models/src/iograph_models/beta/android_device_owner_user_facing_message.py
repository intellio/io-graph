from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerUserFacingMessage(BaseModel):
	defaultMessage: Optional[str] = Field(alias="defaultMessage", default=None,)
	localizedMessages: Optional[list[KeyValuePair]] = Field(alias="localizedMessages", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .key_value_pair import KeyValuePair

