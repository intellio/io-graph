from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MobileContainedAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[MicrosoftStoreForBusinessContainedApp, WindowsUniversalAppXContainedApp],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp
from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp

