from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSWiFiConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[MacOSWiFiConfiguration]]] = Field(alias="value",default=None,)

from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration

