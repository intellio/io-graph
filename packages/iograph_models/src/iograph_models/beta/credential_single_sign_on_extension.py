from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CredentialSingleSignOnExtension(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	configurations: SerializeAsAny[Optional[list[KeyTypedValuePair]]] = Field(alias="configurations",default=None,)
	domains: Optional[list[str]] = Field(alias="domains",default=None,)
	extensionIdentifier: Optional[str] = Field(alias="extensionIdentifier",default=None,)
	realm: Optional[str] = Field(alias="realm",default=None,)
	teamIdentifier: Optional[str] = Field(alias="teamIdentifier",default=None,)

from .key_typed_value_pair import KeyTypedValuePair

