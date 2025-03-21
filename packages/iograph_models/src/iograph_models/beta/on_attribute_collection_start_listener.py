from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionStartListener(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationEventsFlowId: Optional[str] = Field(alias="authenticationEventsFlowId",default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	handler: SerializeAsAny[Optional[OnAttributeCollectionStartHandler]] = Field(alias="handler",default=None,)

from .authentication_conditions import AuthenticationConditions
from .on_attribute_collection_start_handler import OnAttributeCollectionStartHandler

