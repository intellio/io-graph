from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MessageRuleActions(BaseModel):
	assignCategories: Optional[list[str]] = Field(alias="assignCategories", default=None,)
	copyToFolder: Optional[str] = Field(alias="copyToFolder", default=None,)
	delete: Optional[bool] = Field(alias="delete", default=None,)
	forwardAsAttachmentTo: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="forwardAsAttachmentTo", default=None,)
	forwardTo: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="forwardTo", default=None,)
	markAsRead: Optional[bool] = Field(alias="markAsRead", default=None,)
	markImportance: Optional[Importance | str] = Field(alias="markImportance", default=None,)
	moveToFolder: Optional[str] = Field(alias="moveToFolder", default=None,)
	permanentDelete: Optional[bool] = Field(alias="permanentDelete", default=None,)
	redirectTo: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="redirectTo", default=None,)
	stopProcessingRules: Optional[bool] = Field(alias="stopProcessingRules", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .attendee_base import AttendeeBase
from .attendee import Attendee
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .importance import Importance
from .attendee_base import AttendeeBase
from .attendee import Attendee

