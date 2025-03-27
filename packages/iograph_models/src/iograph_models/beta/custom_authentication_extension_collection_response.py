from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CustomAuthenticationExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[OnAttributeCollectionStartCustomExtension, OnAttributeCollectionSubmitCustomExtension, OnOtpSendCustomExtension, OnTokenIssuanceStartCustomExtension]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
from .on_otp_send_custom_extension import OnOtpSendCustomExtension
from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

