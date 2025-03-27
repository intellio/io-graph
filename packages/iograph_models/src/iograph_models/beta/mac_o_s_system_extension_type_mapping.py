from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSSystemExtensionTypeMapping(BaseModel):
	allowedTypes: Optional[MacOSSystemExtensionType | str] = Field(alias="allowedTypes", default=None,)
	teamIdentifier: Optional[str] = Field(alias="teamIdentifier", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .mac_o_s_system_extension_type import MacOSSystemExtensionType

