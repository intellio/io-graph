from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DefaultManagedAppProtection, TargetedManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .default_managed_app_protection import DefaultManagedAppProtection
from .targeted_managed_app_protection import TargetedManagedAppProtection
from .android_managed_app_protection import AndroidManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection

