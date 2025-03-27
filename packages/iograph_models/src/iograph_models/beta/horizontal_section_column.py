from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class HorizontalSectionColumn(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	width: Optional[int] = Field(alias="width", default=None,)
	webparts: Optional[list[Annotated[Union[StandardWebPart, TextWebPart]],Field(discriminator="odata_type")]]] = Field(alias="webparts", default=None,)

from .standard_web_part import StandardWebPart
from .text_web_part import TextWebPart

