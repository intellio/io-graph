from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class MobileAppRelationshipCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[MobileAppDependency, MobileAppSupersedence],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .mobile_app_dependency import MobileAppDependency
from .mobile_app_supersedence import MobileAppSupersedence
