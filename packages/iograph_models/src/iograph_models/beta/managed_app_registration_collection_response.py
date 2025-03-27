from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppRegistrationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidManagedAppRegistration, IosManagedAppRegistration, WindowsManagedAppRegistration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_managed_app_registration import AndroidManagedAppRegistration
from .ios_managed_app_registration import IosManagedAppRegistration
from .windows_managed_app_registration import WindowsManagedAppRegistration

