from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ClassificationError(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	innerError: Optional[ClassificationInnerError] = Field(alias="innerError", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	target: Optional[str] = Field(alias="target", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	details: Optional[list[Annotated[Union[ClassificationError],Field(discriminator="odata_type")]]] = Field(alias="details", default=None,)

from .classification_inner_error import ClassificationInnerError

