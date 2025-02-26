from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AnswerPostRequest(BaseModel):
	callbackUri: Optional[str] = Field(default=None,alias="callbackUri",)
	mediaConfig: Optional[MediaConfig] = Field(default=None,alias="mediaConfig",)
	acceptedModalities: Optional[Modality] = Field(default=None,alias="acceptedModalities",)
	participantCapacity: Optional[int] = Field(default=None,alias="participantCapacity",)
	callOptions: Optional[IncomingCallOptions] = Field(default=None,alias="callOptions",)

from .media_config import MediaConfig
from .modality import Modality
from .incoming_call_options import IncomingCallOptions

