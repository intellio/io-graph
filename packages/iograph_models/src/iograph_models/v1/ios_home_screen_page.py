from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenPage(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	icons: Optional[list[Annotated[Union[IosHomeScreenApp, IosHomeScreenFolder],Field(discriminator="odata_type")]]] = Field(alias="icons", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .ios_home_screen_app import IosHomeScreenApp
from .ios_home_screen_folder import IosHomeScreenFolder

