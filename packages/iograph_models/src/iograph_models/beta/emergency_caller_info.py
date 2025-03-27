from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class EmergencyCallerInfo(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	location: Optional[Union[LocationConstraintItem]] = Field(alias="location", default=None,discriminator="odata_type", )
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	upn: Optional[str] = Field(alias="upn", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .location_constraint_item import LocationConstraintItem

