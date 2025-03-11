from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Download_app_diagnosticsPostRequest(BaseModel):
	request: Optional[PowerliftDownloadRequest] = Field(alias="request",default=None,)

from .powerlift_download_request import PowerliftDownloadRequest

