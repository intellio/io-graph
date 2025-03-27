from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class VerticalSection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	emphasis: Optional[SectionEmphasisType | str] = Field(alias="emphasis", default=None,)
	webparts: Optional[list[Annotated[Union[StandardWebPart, TextWebPart],Field(discriminator="odata_type")]]] = Field(alias="webparts", default=None,)

from .section_emphasis_type import SectionEmphasisType
from .standard_web_part import StandardWebPart
from .text_web_part import TextWebPart

