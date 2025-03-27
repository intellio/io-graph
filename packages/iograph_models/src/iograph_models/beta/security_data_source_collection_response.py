from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDataSourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecuritySiteSource, SecurityUnifiedGroupSource, SecurityUserSource]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_site_source import SecuritySiteSource
from .security_unified_group_source import SecurityUnifiedGroupSource
from .security_user_source import SecurityUserSource

