from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class VerticalSection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.verticalSection"] = Field(alias="@odata.type",)
	emphasis: Optional[SectionEmphasisType | str] = Field(alias="emphasis", default=None,)
	webparts: Optional[list[Annotated[Union[StandardWebPart, TextWebPart],Field(discriminator="odata_type")]]] = Field(alias="webparts", default=None,)

from .section_emphasis_type import SectionEmphasisType
from .standard_web_part import StandardWebPart
from .text_web_part import TextWebPart
