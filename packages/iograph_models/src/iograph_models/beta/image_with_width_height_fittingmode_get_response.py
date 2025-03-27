from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Image_with_width_height_fittingmodeGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)


