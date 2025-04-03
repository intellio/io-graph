from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class VirtualEventWebinarRegistrationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEventWebinarRegistrationConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.virtualEventWebinarRegistrationConfiguration")
	capacity: Optional[int] = Field(alias="capacity", default=None,)
	registrationWebUrl: Optional[str] = Field(alias="registrationWebUrl", default=None,)
	questions: Optional[list[Annotated[Union[VirtualEventRegistrationCustomQuestion, VirtualEventRegistrationPredefinedQuestion],Field(discriminator="odata_type")]]] = Field(alias="questions", default=None,)
	isManualApprovalEnabled: Optional[bool] = Field(alias="isManualApprovalEnabled", default=None,)
	isWaitlistEnabled: Optional[bool] = Field(alias="isWaitlistEnabled", default=None,)

from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
