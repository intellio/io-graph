from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDomainJoinConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsDomainJoinConfiguration]] = Field(alias="value",default=None,)

from .windows_domain_join_configuration import WindowsDomainJoinConfiguration

