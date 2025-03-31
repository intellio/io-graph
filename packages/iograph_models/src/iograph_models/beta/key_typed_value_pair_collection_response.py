from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class KeyTypedValuePairCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[KeyBooleanValuePair, KeyIntegerValuePair, KeyRealValuePair, KeyStringValuePair],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .key_boolean_value_pair import KeyBooleanValuePair
from .key_integer_value_pair import KeyIntegerValuePair
from .key_real_value_pair import KeyRealValuePair
from .key_string_value_pair import KeyStringValuePair
