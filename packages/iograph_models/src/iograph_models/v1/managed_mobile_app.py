from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class ManagedMobileApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedMobileApp"] = Field(alias="@odata.type", default="#microsoft.graph.managedMobileApp")
	mobileAppIdentifier: Optional[Union[AndroidMobileAppIdentifier, IosMobileAppIdentifier]] = Field(alias="mobileAppIdentifier", default=None,discriminator="odata_type", )
	version: Optional[str] = Field(alias="version", default=None,)

from .android_mobile_app_identifier import AndroidMobileAppIdentifier
from .ios_mobile_app_identifier import IosMobileAppIdentifier
