from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class MacOSAzureAdSingleSignOnExtension(BaseModel):
	odata_type: Literal["#microsoft.graph.macOSAzureAdSingleSignOnExtension"] = Field(alias="@odata.type", default="#microsoft.graph.macOSAzureAdSingleSignOnExtension")
	bundleIdAccessControlList: Optional[list[str]] = Field(alias="bundleIdAccessControlList", default=None,)
	configurations: Optional[list[Annotated[Union[KeyBooleanValuePair, KeyIntegerValuePair, KeyRealValuePair, KeyStringValuePair],Field(discriminator="odata_type")]]] = Field(alias="configurations", default=None,)
	enableSharedDeviceMode: Optional[bool] = Field(alias="enableSharedDeviceMode", default=None,)

from .key_boolean_value_pair import KeyBooleanValuePair
from .key_integer_value_pair import KeyIntegerValuePair
from .key_real_value_pair import KeyRealValuePair
from .key_string_value_pair import KeyStringValuePair
