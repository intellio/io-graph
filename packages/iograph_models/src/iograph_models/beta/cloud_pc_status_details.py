from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcStatusDetails(BaseModel):
	additionalInformation: Optional[list[KeyValuePair]] = Field(alias="additionalInformation", default=None,)
	code: Optional[str] = Field(alias="code", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .key_value_pair import KeyValuePair

