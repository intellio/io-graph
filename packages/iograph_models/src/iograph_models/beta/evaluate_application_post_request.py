from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Evaluate_applicationPostRequest(BaseModel):
	contentInfo: Optional[ContentInfo] = Field(alias="contentInfo", default=None,)
	labelingOptions: Optional[LabelingOptions] = Field(alias="labelingOptions", default=None,)

from .content_info import ContentInfo
from .labeling_options import LabelingOptions

