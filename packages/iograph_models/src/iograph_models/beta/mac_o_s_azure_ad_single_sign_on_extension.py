from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSAzureAdSingleSignOnExtension(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	bundleIdAccessControlList: Optional[list[str]] = Field(alias="bundleIdAccessControlList",default=None,)
	configurations: SerializeAsAny[Optional[list[KeyTypedValuePair]]] = Field(alias="configurations",default=None,)
	enableSharedDeviceMode: Optional[bool] = Field(alias="enableSharedDeviceMode",default=None,)

from .key_typed_value_pair import KeyTypedValuePair

