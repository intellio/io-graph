from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WebPartCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[StandardWebPart, TextWebPart]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .standard_web_part import StandardWebPart
from .text_web_part import TextWebPart

