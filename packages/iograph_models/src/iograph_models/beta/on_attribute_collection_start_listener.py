from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionStartListener(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onAttributeCollectionStartListener"] = Field(alias="@odata.type", default="#microsoft.graph.onAttributeCollectionStartListener")
	authenticationEventsFlowId: Optional[str] = Field(alias="authenticationEventsFlowId", default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	handler: Optional[Union[OnAttributeCollectionStartCustomExtensionHandler]] = Field(alias="handler", default=None,discriminator="odata_type", )

from .authentication_conditions import AuthenticationConditions
from .on_attribute_collection_start_custom_extension_handler import OnAttributeCollectionStartCustomExtensionHandler

