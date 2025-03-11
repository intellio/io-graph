from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PreviewPostRequest(BaseModel):
	viewer: Optional[str] = Field(alias="viewer",default=None,)
	chromeless: Optional[bool] = Field(alias="chromeless",default=None,)
	allowEdit: Optional[bool] = Field(alias="allowEdit",default=None,)
	page: Optional[str] = Field(alias="page",default=None,)
	zoom: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

