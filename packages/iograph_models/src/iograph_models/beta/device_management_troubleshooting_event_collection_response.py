from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementTroubleshootingEventCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AppleVppTokenTroubleshootingEvent, EnrollmentTroubleshootingEvent, MobileAppTroubleshootingEvent],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

