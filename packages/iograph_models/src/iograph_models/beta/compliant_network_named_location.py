from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CompliantNetworkNamedLocation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	compliantNetworkType: Optional[CompliantNetworkType | str] = Field(alias="compliantNetworkType",default=None,)
	isTrusted: Optional[bool] = Field(alias="isTrusted",default=None,)

from .compliant_network_type import CompliantNetworkType

