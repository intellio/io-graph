from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class Update_relationshipsPostRequest(BaseModel):
	relationships: Optional[list[Annotated[Union[MobileAppDependency, MobileAppSupersedence],Field(discriminator="odata_type")]]] = Field(alias="relationships", default=None,)

from .mobile_app_dependency import MobileAppDependency
from .mobile_app_supersedence import MobileAppSupersedence
