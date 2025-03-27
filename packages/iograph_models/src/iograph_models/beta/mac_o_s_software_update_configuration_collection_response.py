from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSSoftwareUpdateConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MacOSSoftwareUpdateConfiguration]] = Field(alias="value", default=None,)

from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration

