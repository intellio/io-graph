from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppPolicyDeploymentSummaryPerApp(BaseModel):
	configurationAppliedUserCount: Optional[int] = Field(alias="configurationAppliedUserCount", default=None,)
	mobileAppIdentifier: Optional[Union[AndroidMobileAppIdentifier, IosMobileAppIdentifier]] = Field(alias="mobileAppIdentifier", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .android_mobile_app_identifier import AndroidMobileAppIdentifier
from .ios_mobile_app_identifier import IosMobileAppIdentifier

