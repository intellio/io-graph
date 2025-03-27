from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IosHomeScreenApp, IosHomeScreenFolder],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .ios_home_screen_app import IosHomeScreenApp
from .ios_home_screen_folder import IosHomeScreenFolder

