from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AuthenticationEventListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[OnAttributeCollectionListener, OnAuthenticationMethodLoadStartListener, OnInteractiveAuthFlowStartListener, OnTokenIssuanceStartListener, OnUserCreateStartListener],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .on_attribute_collection_listener import OnAttributeCollectionListener
from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
from .on_user_create_start_listener import OnUserCreateStartListener
