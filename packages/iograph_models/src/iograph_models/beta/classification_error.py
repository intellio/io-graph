from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClassificationError(BaseModel):
	code: Optional[str] = Field(alias="code",default=None,)
	innerError: Optional[ClassificationInnerError] = Field(alias="innerError",default=None,)
	message: Optional[str] = Field(alias="message",default=None,)
	target: Optional[str] = Field(alias="target",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	details: SerializeAsAny[Optional[list[ClassifcationErrorBase]]] = Field(alias="details",default=None,)

from .classification_inner_error import ClassificationInnerError
from .classifcation_error_base import ClassifcationErrorBase

