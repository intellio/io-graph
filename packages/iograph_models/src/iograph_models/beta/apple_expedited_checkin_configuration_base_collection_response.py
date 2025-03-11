from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppleExpeditedCheckinConfigurationBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AppleExpeditedCheckinConfigurationBase]]] = Field(alias="value",default=None,)

from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase

