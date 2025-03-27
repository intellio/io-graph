from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSRedirectSingleSignOnExtension(BaseModel):
	odata_type: Literal["#microsoft.graph.macOSRedirectSingleSignOnExtension"] = Field(alias="@odata.type", default="#microsoft.graph.macOSRedirectSingleSignOnExtension")
	configurations: Optional[list[Annotated[Union[KeyBooleanValuePair, KeyIntegerValuePair, KeyRealValuePair, KeyStringValuePair]],Field(discriminator="odata_type")]]] = Field(alias="configurations", default=None,)
	extensionIdentifier: Optional[str] = Field(alias="extensionIdentifier", default=None,)
	teamIdentifier: Optional[str] = Field(alias="teamIdentifier", default=None,)
	urlPrefixes: Optional[list[str]] = Field(alias="urlPrefixes", default=None,)

from .key_boolean_value_pair import KeyBooleanValuePair
from .key_integer_value_pair import KeyIntegerValuePair
from .key_real_value_pair import KeyRealValuePair
from .key_string_value_pair import KeyStringValuePair

