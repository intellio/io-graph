from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_evaluate_applicationPostRequest(BaseModel):
	contentInfo: Optional[SecurityContentInfo] = Field(alias="contentInfo", default=None,)
	labelingOptions: Optional[SecurityLabelingOptions] = Field(alias="labelingOptions", default=None,)

from .security_content_info import SecurityContentInfo
from .security_labeling_options import SecurityLabelingOptions
