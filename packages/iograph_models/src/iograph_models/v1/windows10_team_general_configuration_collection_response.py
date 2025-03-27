from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10TeamGeneralConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10TeamGeneralConfiguration]] = Field(alias="value", default=None,)

from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration

