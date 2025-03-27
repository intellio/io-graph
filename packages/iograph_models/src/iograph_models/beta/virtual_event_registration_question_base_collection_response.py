from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventRegistrationQuestionBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[VirtualEventRegistrationCustomQuestion, VirtualEventRegistrationPredefinedQuestion]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

