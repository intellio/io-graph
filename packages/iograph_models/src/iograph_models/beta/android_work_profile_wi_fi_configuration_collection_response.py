from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidWorkProfileWiFiConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AndroidWorkProfileWiFiConfiguration]]] = Field(alias="value",default=None,)

from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration

