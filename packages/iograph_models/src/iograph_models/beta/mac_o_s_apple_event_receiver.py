from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSAppleEventReceiver(BaseModel):
	allowed: Optional[bool] = Field(alias="allowed",default=None,)
	codeRequirement: Optional[str] = Field(alias="codeRequirement",default=None,)
	identifier: Optional[str] = Field(alias="identifier",default=None,)
	identifierType: Optional[MacOSProcessIdentifierType | str] = Field(alias="identifierType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

