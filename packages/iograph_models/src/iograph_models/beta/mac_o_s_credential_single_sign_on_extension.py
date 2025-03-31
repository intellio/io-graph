from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class MacOSCredentialSingleSignOnExtension(BaseModel):
	odata_type: Literal["#microsoft.graph.macOSCredentialSingleSignOnExtension"] = Field(alias="@odata.type", default="#microsoft.graph.macOSCredentialSingleSignOnExtension")
	configurations: Optional[list[Annotated[Union[KeyBooleanValuePair, KeyIntegerValuePair, KeyRealValuePair, KeyStringValuePair],Field(discriminator="odata_type")]]] = Field(alias="configurations", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	extensionIdentifier: Optional[str] = Field(alias="extensionIdentifier", default=None,)
	realm: Optional[str] = Field(alias="realm", default=None,)
	teamIdentifier: Optional[str] = Field(alias="teamIdentifier", default=None,)

from .key_boolean_value_pair import KeyBooleanValuePair
from .key_integer_value_pair import KeyIntegerValuePair
from .key_real_value_pair import KeyRealValuePair
from .key_string_value_pair import KeyStringValuePair
